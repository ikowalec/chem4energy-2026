# Writing input files for QM codes is a commons task.
# Here is an example of how to write an input file for Quantum Espresso using ASE. 
# The same approach can be used for other QM codes as well.
# QM calculations can be directly called from ASE using the corresponding calculator,
#  but here we show how to write an input file which can be used for running calculations outside of ASE.

from ase.io import read, write


# Read the atomic structure
atoms = read("examples/data/TiNiO3_slab.cif")

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