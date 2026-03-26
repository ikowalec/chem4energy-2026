# Chem4Energy 2026

Materials for the Chem4Energy conference hands-on workshop on ASE/MACE.

## Start Here (First-Time Users)

## Prerequisites

Python 3.11 is recommended for compatibility with typical HPC software stacks.

1. Install Python 3.11: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
2. Install Git: https://git-scm.com/install/windows

If you are not familiar with Python at all, please follow the official Cardiff University tutorials
by Dr Tom Slater: https://github.com/TomSlater/Introduction-To-Programming-with-Python

If you are new to coding projects, follow these steps in order.

1. Open VS Code.
2. Open the Command Palette (`Ctrl+Shift+P`) and run `Git: Clone`.
3. Paste the GitHub repository link:

```text
https://github.com/ikowalec/chem4energy-2026.git
```
4. You will be prompted to register/sign in on GitHub, please make a free account if you don't have one.
5. Choose where to save the project on your computer.
6. Click `Open` when VS Code asks to open the cloned repository.



## VS Code (PowerShell) Setup

Press CTRL + SHIFT + '
This opens a terminal where you get execute the command below:

Run this command once to allow Python virtual environment activation in VS Code PowerShell:

```powershell
Set-ExecutionPolicy Bypass -Scope CurrentUser -Force
```

Then create and activate a virtual environment in the project folder (or via Create venv menu):

```powershell
python -m venv .venv
```

If you created the venv via VS Code window there is a good chance it pick up the requirements file and downloaded the relevant libraries. If not, activate the environment and install the libraries from the file:

```powershell
.\.venv\Scripts\Activate.ps1
```

```powershell
pip install -r requirements.txt
```

# ASE official tutorials:
https://ase-lib.org/examples_generated/index.html

# Topics to cover:
- (x) Setting up VS Code 
- (x) Installing required libraries and cloning repo 
- (x) Rendering images of structures 
- (x) Surface cutting
- (x) Saving structures as input for qm codes 
- ( ) ASE as a teaching tool
- ( ) Material doping and atomic substitutions
- ( ) MLIPs - Using MACE as a calculator 
- ( ) How can we train MACE models on VASP (or any QM) calculations?
- ( ) Preparing data for MACE model tuning
- ( ) Automatic adsorbate placement
- ( ) Cluster discovery
- ( ) Connectivity matrix and nearest neighbors analysis
- ( ) Similarity matrices -> ensuring a diverse dataset
- ( ) ASE and Cluster Expansion (CELL)

# Calculations via ASE:
- () TS search (+ method breakdown)
- () vibrational frequency calculations
- () ?

