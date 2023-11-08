# Python Package Exercise

A little exercise to create a Python package, build it, test it, distribute it, and use it. See [instructions](./instructions.md) for details.

![Github badge displaying the build status of this repository](https://github.com/software-students-fall2023/3-python-package-exercise-17/actions/workflows/python-app.yml/badge.svg)


## Authors
Ethan Delgado: ethan-delgado
Eric Cho: ec3566
Chang Liu: Lcccc123
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

# Contribution Instructions
First you must download the package to your local machine:
```
pip install 3-python-package-exercise-17==0.1.0
```
You can now make changes to the package as you wish. Here is some documentation to get you started...
## Classes and Functions

### `SimpleWordle` class

#### `__init__(self, word_list)`

Initializes a new game of SimpleWordle.

- **Parameters**:
  - `word_list` (list of str): A list of possible target words.
- **Attributes**:
  - `target_word` (str): The word that players try to guess.
  - `word_length` (int): The length of the target word.
  - `attempts` (int): The number of attempts the player has made.

#### `guess(self, word)`

Processes a user's guess and provides feedback.

- **Parameters**:
  - `word` (str): The word guessed by the user.
- **Returns**:
  - A string with feedback symbols (🟩, 🟨, ⬛) for each letter in the guess.

#### `play(self)`

Starts and handles the game loop for SimpleWordle.

- **Returns**:
  - `1` if the player guesses the word correctly, `0` otherwise.

### `start_game(word_list_path='word_list.txt')`

Creates a new game of SimpleWordle using a word list from a file and starts the game.

- **Parameters**:
  - `word_list_path` (str): The path to the file containing the word list.
- **Returns**:
  - `0` to indicate the game has ended.

### `add_word(word, word_list_path='word_list.txt')`

Adds a new word to the word list file.

- **Parameters**:
  - `word` (str): The word to be added.
  - `word_list_path` (str): The path to the file containing the word list.

### `remove_word(word, word_list_path='word_list.txt')`

Removes a word from the word list file.

- **Parameters**:
  - `word` (str): The word to be removed.
  - `word_list_path` (str): The path to the file containing the word list.

### `show_word_list(word_list_path='word_list.txt')`

Prints out all words in the word list file.

- **Parameters**:
  - `word_list_path` (str): The path to the file containing the word list.

## Example Usage

```python
# Example program using the SimpleWordle package functions

# First, make sure to import the package or functions if they are in a separate file
# from simple_wordle_package import start_game, add_word, remove_word, show_word_list

# Add a word to the word list
add_word('apple')

# Remove a word from the word list
remove_word('orange')

# Show the current word list
show_word_list()

# Start the game with the word list
start_game()


[Link to PYPI webpage of the app](https://pypi.org/project/3-python-package-exercise-17/0.1.0/)