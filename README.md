## Chem4Energy 2026

Materials for the Chem4Energy conference hands-on workshops open-source software for computational chemistry.

List of contributors: 
- Igor Kowalec (main author)
- Thomas Hill

## Start Here (First-Time Users)

Please attempt to go through the steps bellow 

# Prerequisites:
- A working installation of VS Code, Python and Git. Follow the [First Steps guide](initial_setup.md).
- Basic understanding of Python, see more information in [FAQ](FAQ.md).

# ASE official tutorials:

Atomic Simulation Environment provides an ecosystem for chemical structure analysis and simulation routines.

```text
https://ase-lib.org/examples_generated/index.html
```

# Topics to cover:
- (x) Setting up VS Code 
- (x) Installing required libraries and cloning repository
- (x) Rendering images of structures 
- (x) Surface cutting
- (x) Saving structures as input for qm codes 
- ( ) Simulating XRD patterns from bulk structures
- ( ) ASE as a teaching tool and data production
- ( ) Material doping and atomic substitutions
- ( ) Machine-learned interatomic potentials - Using [MACE](https://mace-docs.readthedocs.io/en/latest/guide/guide.html)
- ( ) How can we train MACE models on VASP (or any QM) calculations?
- ( ) Preparing data for MACE model tuning
- ( ) Automatic adsorbate placement
- ( ) Cluster discovery
- ( ) Connectivity matrix and nearest neighbors analysis
- ( ) Similarity matrices -> ensuring a diverse dataset
- ( ) ASE and Cluster Expansion (CELL)
See original paper by S. Rigamonti <i>et al.</i>: [CELL: a Python package for cluster expansion with a focus on complex alloys](https://www.nature.com/articles/s41524-024-01363-x)

Teaching material adapted from: https://sol.physik.hu-berlin.de/cell/tutorials/tutorials.html

Schedule:
Mondays 2pm UK time (4pm SA)

- ASE/MACE setup - Using machine-learned interatomic potentials as a simulation driver
- ASE/MACE ML-potential training (external speaker: Dr Kushagra Agrawal)
- ASE/RDKit - using structural databases and conformer discovery
- ASE/pymatgen - cutting and modifying material surface
- ASE/CELL - Cluster Expansion method
- ASE/acat - adsorbate placement on gas-phase clusters and surfaces
- ASE/REMatch/SOAP - Structural similarity, cluster discovery
- ASE/CatLearn - ML-accelerated optimisation and transition-state workflows

- ASE/QM - Interfacing ASE with QM codes for data production

Gas theme:
- creating adsorbates, databases, vib freq
- TD-DFT - NWChem, PySCF, Siesta, ORCA, FHI-aims - free for academic use

Bulk techniques:
- atomic substitution
- unit cell optimisation
- vacancy generation
- Cluster Expansion

Surface theme:
- Slab convergence strategy (thickness, vacuum, k-point density).
- Adsorption site enumeration and adsorption energy maps.
- Surface diffusion barriers (NEB on slabs).
- Surface phase diagrams vs temperature/pressure.
- Cluster Expansion
- Cluster Discovery

Phase-agnostic:
- MACE use
- MACE retraining


