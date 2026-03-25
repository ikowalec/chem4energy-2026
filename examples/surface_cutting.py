from ase.io import read
from ase.io import write
from ase.visualize import view
from ase.constraints import FixAtoms
import sys
sys.path.append('.') # add the current directory to the system path to import helper functions

from helper_functions import generate_pymatgen_surface as surface

# Read in the structure
bulk_model = read("examples/data/TiNiO3.cif")

# Inspect the  bulk structure via GUI
# view(bulk_model)

vacuum = 20 # in Angstrom
slabs = surface(bulk_model, 
               layers=1, # use 2 to to see more terminations
               symmetric=True, 
               miller_index=(0, 0, 1), 
               vacuum=vacuum, 
               spin=True,
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
slab.set_initial_charges(list_of_charges)
"""

# Example structure writing
atoms = slabs[0] 

# make a supercell
atoms = atoms.repeat((2, 2, 1)) 

# view(atoms)

write("examples/data/TiNiO3_slab.cif", atoms) # save as .cif file
