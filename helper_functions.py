def generate_pymatgen_surface(
    bulk_model,
    layers=2,
    symmetric=True,
    miller_index=(1, 0, 0),
    vacuum=20,
    spin=False,
    tol=0.01,
):
    """
    Generate slab models for a given Miller index using pymatgen, then return ASE Atoms objects.

    This function is useful for multicomponent materials (oxides, sulfides, perovskites, etc.),
    where a single facet can yield multiple chemically distinct terminations.

    Parameters
    ----------
    bulk_model : ase.Atoms
        Conventional bulk unit cell to cut slabs from.
    layers : int, default=2
        Slab thickness in pymatgen "unit planes" (not equivalent to ASE atomic layers).
    symmetric : bool, default=True
        If True, request symmetrized slabs from pymatgen.
    miller_index : tuple[int, int, int], default=(1, 0, 0)
        Facet orientation.
    vacuum : float, default=20
        Vacuum thickness in Angstrom along the slab normal (z-axis after conversion).
    spin : bool, default=False
        If True, transfer initial magnetic moments from ASE to pymatgen structure.
    tol : float, default=0.01
        Termination tolerance (`ftol`) used by pymatgen when enumerating slabs.
    """
    from pymatgen.core.surface import SlabGenerator
    from pymatgen.io.ase import AseAtomsAdaptor

    # Convert ASE Atoms to pymatgen Structure so we can use SlabGenerator.
    structure = AseAtomsAdaptor.get_structure(bulk_model)

    # Transfer oxidation states from initial charges if they are set on the ASE atoms.
    charge_list = list(bulk_model.get_initial_charges())
    structure.add_oxidation_state_by_site(charge_list)

    # Optionally transfer spin information from initial magnetic moments.
    if spin:
        spin_list = list(bulk_model.get_initial_magnetic_moments())
        structure.add_spin_by_site(spin_list)

    # Build slab candidates for the target Miller index.
    slabgen = SlabGenerator(
        structure,
        miller_index=miller_index,
        min_slab_size=layers,
        min_vacuum_size=vacuum,
        center_slab=True,
        in_unit_planes=True,
        lll_reduce=True,
    )
    slabs = slabgen.get_slabs(ftol=tol, symmetrize=symmetric)

    # Convert each pymatgen Slab back to ASE and ensure vacuum/wrapping are clean.
    slabs_ase = []
    for slab in slabs:
        slab_atoms = AseAtomsAdaptor.get_atoms(slab.get_orthogonal_c_slab())
        slab_atoms.center(vacuum=vacuum, axis=2)
        slab_atoms.wrap()
        slabs_ase.append(slab_atoms)

    return slabs_ase
