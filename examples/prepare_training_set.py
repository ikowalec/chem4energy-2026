#!/usr/bin/env python3
"""Convert an ASE trajectory to MACE-ready extended XYZ training data.

Example:
    python examples/prepare_training_set.py opt.traj training.extxyz

The output stores reference labels as:
    atoms.info["ref_energy"]
    atoms.arrays["ref_forces"]

This avoids using the conventional "energy" and "forces" names, which can
clash with ASE calculator results when the file is read later.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Read structures from an ASE .traj file and write .extxyz with ref_energy/ref_forces labels."
    )
    parser.add_argument("input", help="Input ASE trajectory file, for example opt.traj")
    parser.add_argument(
        "output",
        nargs="?",
        help="Output extended XYZ file. Defaults to the input name with .extxyz suffix.",
    )
    parser.add_argument(
        "--index",
        default=":",
        help='ASE frame selector. Use ":" for all frames, "-1" for the last frame, or "0:10" for a slice.',
    )
    parser.add_argument(
        "--energy-key",
        default="ref_energy",
        help="Metadata key used for the saved reference energy.",
    )
    parser.add_argument(
        "--forces-key",
        default="ref_forces",
        help="Array key used for the saved reference forces.",
    )
    parser.add_argument(
        "--source-energy-key",
        default=None,
        help="Optional existing atoms.info key to read energies from before calculator results.",
    )
    parser.add_argument(
        "--source-forces-key",
        default=None,
        help="Optional existing atoms.arrays key to read forces from before calculator results.",
    )
    return parser.parse_args()


def as_image_list(images: Any) -> list[Any]:
    from ase import Atoms

    if isinstance(images, Atoms):
        return [images]
    return list(images)


def scalar_energy(value: object) -> float:
    import numpy as np

    return float(np.asarray(value).reshape(()))


def get_energy(atoms: Any, source_key: str | None, target_key: str) -> float:
    info_keys = [source_key, target_key, "energy"]
    for key in info_keys:
        if key and key in atoms.info:
            return scalar_energy(atoms.info[key])

    if atoms.calc is not None:
        results = getattr(atoms.calc, "results", {})
        if "energy" in results:
            return scalar_energy(results["energy"])

    return scalar_energy(atoms.get_potential_energy())


def get_forces(atoms: Any, source_key: str | None, target_key: str) -> Any:
    import numpy as np

    array_keys = [source_key, target_key, "forces"]
    for key in array_keys:
        if key and key in atoms.arrays:
            forces = np.asarray(atoms.arrays[key], dtype=float)
            break
    else:
        if atoms.calc is not None:
            results = getattr(atoms.calc, "results", {})
            if "forces" in results:
                forces = np.asarray(results["forces"], dtype=float)
            else:
                forces = np.asarray(atoms.get_forces(), dtype=float)
        else:
            forces = np.asarray(atoms.get_forces(), dtype=float)

    expected_shape = (len(atoms), 3)
    if forces.shape != expected_shape:
        raise ValueError(f"Expected forces with shape {expected_shape}, got {forces.shape}")
    return forces


def prepare_image(
    atoms: Any,
    energy_key: str,
    forces_key: str,
    source_energy_key: str | None,
    source_forces_key: str | None,
) -> Any:
    energy = get_energy(atoms, source_energy_key, energy_key)
    forces = get_forces(atoms, source_forces_key, forces_key)

    clean = atoms.copy()
    clean.calc = None

    clean.info[energy_key] = energy
    clean.arrays[forces_key] = forces

    if energy_key != "energy":
        clean.info.pop("energy", None)
    if forces_key != "forces":
        clean.arrays.pop("forces", None)

    return clean


def main() -> None:
    args = parse_args()
    from ase.io import read, write

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path.with_suffix(".extxyz")

    images = as_image_list(read(input_path, index=args.index))
    if not images:
        raise ValueError(f"No structures were read from {input_path}")

    prepared = []
    for frame_number, atoms in enumerate(images):
        try:
            prepared.append(
                prepare_image(
                    atoms,
                    energy_key=args.energy_key,
                    forces_key=args.forces_key,
                    source_energy_key=args.source_energy_key,
                    source_forces_key=args.source_forces_key,
                )
            )
        except Exception as exc:
            raise RuntimeError(f"Could not prepare frame {frame_number} from {input_path}") from exc

    write(output_path, prepared, format="extxyz")
    print(f"Wrote {len(prepared)} structures to {output_path}")
    print(f"Energy key: {args.energy_key}")
    print(f"Forces key: {args.forces_key}")


if __name__ == "__main__":
    main()
