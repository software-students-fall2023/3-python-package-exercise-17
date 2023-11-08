# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

## App discription
A simple Wordle-like game to play in the terminal.

## Set Up
Set up Pipenv:
```
pip install pipenv
pipenv install --dev
```
Write and Run Tests with Pytest:
```
pipenv run pytest
```
Build Package Artifacts with build:
```
pip install build
python -m build --wheel
```
Upload to PYPI using twine:
```
pip install twine
twine upload dist/*
```
[Link to PYPI webpage of the app](https://pypi.org/project/3-python-package-exercise-17/0.1.0/)