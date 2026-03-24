# Chem4Energy 2026

Materials for the Chem4Energy conference hands-on workshop on ASE/MACE.

## Start Here (First-Time Users)

If you are new to coding projects, follow these steps in order.

1. Open VS Code.
2. Open the Command Palette (`Ctrl+Shift+P`) and run `Git: Clone`.
3. Paste the GitHub repository link:

```text
https://github.com/ikowalec/chem4energy-2026.git
```

4. Choose where to save the project on your computer.
5. Click `Open` when VS Code asks to open the cloned repository.

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

