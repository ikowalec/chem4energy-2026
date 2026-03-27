# First configuration

Python 3.11 is recommended for compatibility with typical HPC software stacks.

1. Install Python 3.11: https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
2. Install Git: https://git-scm.com/install/windows


If you are new to coding projects, follow these steps in order.

1. Open VS Code.
2. Open the Command Palette (`Ctrl + Shift + P`) and run `Git: Clone`.
3. Paste the GitHub repository link:

```text
https://github.com/ikowalec/chem4energy-2026.git
```
4. You will be prompted to register/sign in on GitHub, please make a free account if you don't have one.
5. Choose where to save the project on your computer.
6. Click `Open` when VS Code asks to open the cloned repository.


## VS Code Setup (initial)
To open the Extensions menu, press `Ctrl + Shift + X`, the menu should appear on the left side.

Search for and install the following extensions:
- `Python`
- `Jupyter `

If you do not know Python, you will find useful information in the [FAQ document](FAQ.md).


To open the terminal window press `Ctrl + Shift + '`, the terminal window will open in a panel on the bottom.

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

# Finally
The code in this repository is evolving. Before every session make sure you download the newest version of the code, this is done by:
- Clicking the Source Control panel on the left (also `Ctrl + Shift + G`)
- Click three dots `...` and choose the `Pull` option - Git will automatically synchronise the code. 