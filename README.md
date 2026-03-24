# Chem4Energy 2026

Materials for the Chem4Energy conference hands-on workshop on ASE/MACE.

## Start Here (First-Time Users)

If you are new to coding projects, follow these steps in order.

1. Open a terminal (PowerShell on Windows).
2. Move to the folder where you want to store the project, for example:

```powershell
cd C:\Users\<your-username>\Documents\GitHub
```

3. Clone the project using the GitHub link:

```powershell
git clone https://github.com/ikowalec/chem4energy-2026.git
cd chem4energy-2026
```

4. Open the project in VS Code:

```powershell
code .
```

## Prerequisites

Python 3.11 is recommended for compatibility with typical HPC software stacks.

1. Install Python 3.11: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
2. Install Git: https://git-scm.com/install/windows

## VS Code (PowerShell) Setup

Run this command once to allow Python virtual environment activation in VS Code PowerShell:

```powershell
Set-ExecutionPolicy Bypass -Scope CurrentUser -Force
```

Then create and activate a virtual environment in the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

