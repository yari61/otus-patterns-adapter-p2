# Initialization
## Clone project
```
git clone https://github.com/yari61/otus-patterns-adapter-p2.git
cd otus-patterns-adapter-p2
```

## Virtual environment
It is recommended to create a virtual environment at first (.venv for example)
```
python -m venv .venv
```

Then activate it with 
- ```source .venv/bin/activate```
on Unix-like systems, or
- ```.venv\Scripts\activate```
if Your system runs Windows

## Installation
To install the package run the next command in your virtual environment (p1 installs automatically with p2)
```
pip install -e .
```

## Testing
To run tests execute the command listed below
```
python -m unittest
```

# Project description
## Goal
The main goal of this program is to generate two matrices, dump them to a file and summarize these matrices with the p1 program using the adapter object.
## Adapter
Adapter object is stored in ```matrix_gen.operations.summarize```. It calls the p1 program, which is installed in current python environment as a dependency of the p2 program, as a subprocess.

# Quick start guide
## Command line interface
To generate a matrix pair and get sum of these matrix run the following command
```
python -m matrix_gen -o /path/to/output/file
```