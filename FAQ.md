# Frequently asked questions

### How do I start? I do not even know Python!

If you are not familiar with Python, please follow the [official Cardiff University tutorials](https://github.com/TomSlater/Introduction-To-Programming-with-Python) by Dr Tom Slater.

Open a new VS Code window and follow the steps 1-6 above, this time using this link in step 3.:
```text
https://github.com/TomSlater/Introduction-To-Programming-with-Python.git
```

`Pre-reading.ipynb` - learn how to work with interactive code in Jupyter notebooks

Then proceed to sessions 1 & 2, allowing 1-3 hours for each, depending on experience.

Alternatively, if you would like to follow a more comprehensive course on which Dr Slater's materials are based,
please see the materials from [The University of Edinburgh](https://github.com/Edinburgh-Chemistry-Teaching/Data-driven-chemistry). 

### Installing MACE
The recommended way of installing MACE is:
```bash
pip install --upgrade pip
pip install mace-torch
```
See official [documentation](https://mace-docs.readthedocs.io/en/latest/guide/installation.html).

### Updating the virtual environment with new packages
If new dependendencies have been added since the last tutorial, you can download them by using the pip package manager

```bash
. .\.venv\Scripts\activate
pip install -r requirements.txt
```