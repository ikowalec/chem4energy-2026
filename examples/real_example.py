from ase.io import read
from ase.io import write
from ase.visualize import view
from ase.constraints import FixAtoms
import sys
sys.path.append('.') # add the current directory to the system path to import helper functions

from helper_functions import generate_pymatgen_surface as surface

# Read in the structure
bulk_model = read("examples/TiNiO3.cif")

# inspect the  bulk structure via GUI
# view(bulk_model)
vacuum = 20 # in Angstrom
slabs = surface(bulk_model, 
               layers=1, # use 2 to to see more terminations
               symmetric=True, 
               miller_index=(0, 0, 1), 
               vacuum=vacuum, 
               spin=False,
			   tol=0.01)

# Constrain the bottom 6 Angstroms of the slab to mimic bulk behavior during relaxation. 
for slab in slabs:
    c = FixAtoms(mask=[atom.index for atom in slab if atom.z < vacuum + 6]) 
    slab.set_constraint(c)

# Adjust initial charges
species_charges = {'Ti': 4, 'Ni': 2, 'O': -2} # example charges for each species
for slab in slabs:
    for atom in slab:
        atom.charge = species_charges.get(atom.symbol) # set charge based on species, default to 0 if not found

"""
# If there is a pre-supplied list of charges.
list_of_charges = []
slab.set_initial_charges(list_of_charges) # set the initial charges for the slab
"""
# view(slabs)

# example structure writing
atoms = slabs[0] # take the first slab for demonstration

# make a supercell
atoms = atoms.repeat((2, 2, 1)) 

view(atoms)

# Define input parameters for Quantum Espresso
input_data = {
    'calculation': 'relax',
    'restart_mode': 'from_scratch',
    'tprnfor': True,
    'etot_conv_thr': 1e-5,
    'forc_conv_thr': 1e-4,
    'ecutwfc': 60,
    'ecutrho': 480,
    'input_dft': 'rpbe',
    'vdw_corr': 'dft-d3',
    'occupations': 'smearing',
    'degauss': 0.01,
    'smearing': 'cold',
    'conv_thr': 1e-8,
    'mixing_mode': 'local-TF',
    'mixing_beta': 0.35,
    'diagonalization': 'david',
    'ion_dynamics': 'bfgs',
    'bfgs_ndim': 6,
    'startingwfc': 'random',
}  

# This flat dictionary will be converted to a nested dictionary where, 
# for example, "calculation" will be put into the "control" section

pseudopotentials = {
    'Ti': 'Ti.pz-vbc.UPF',
    'Ni': 'Ni.pz-vbc.UPF',
    'O': 'O.pz-vbc.UPF'
}

write('examples/pw.in', 
      atoms, 
      input_data=input_data, 
      pseudopotentials=pseudopotentials, 
      format='espresso-in'
    )

"""
To use Quantum Espresso via ASE see: https://ase-lib.org/ase/calculators/espresso.html

# Hubbard is not implemented in the write_espresso_in function, we can add it manually
additional_cards = ['HUBBARD (ortho-atomic)', 'U Mn-3d 5.0', 'U Ni-3d 6.0']

write(
    'pw_hubbard.in',
    atoms,
    input_data=input_data,
    additional_cards=additional_cards,
    format='espresso-in',
)
"""