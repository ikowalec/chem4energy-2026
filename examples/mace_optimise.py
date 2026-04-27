# Author: Thomas Hill

from mace.calculators import mace_mp
from ase.io import read
from ase.build import bulk  
from ase.io import read, write

# First make sure you have the following installed:
# ase torch mace-torch torch-dftd

### Build bulk CeO2 (fluorite) ###
atoms = bulk("CeO2", "fluorite", a=5.41, cubic=True)
write("structure.cif", atoms, format='cif')
write("structure.xyz", atoms, format='xyz')
write("POSCAR", atoms, format='vasp')

### READING STRUCTURES ###
atoms = read(r"POSCAR", format='vasp')
atoms =read(r"structure.cif", format='cif')
atoms = read(r"structure.xyz", format='xyz')

### CREATE MACE MP (Materials Project) ###
MODEL = 'small'
#MODEL = r"MACE-OMAT-0-medium.model"
PARAMS = {'model': MODEL,
          'dispersion': False,
          'default_dtype': 'float64',
          'device': 'cpu'}

calc = mace_mp(**PARAMS)

### Perform a geometry optimisation ###
from ase.optimize import BFGS
atoms.calc = calc
opt = BFGS(atoms, trajectory='opt.traj', logfile='opt.log')
opt.run(fmax=0.01, steps=500)