# Auto Commit Name Generator

This project contains a script that generates a unique git commit name based on the changes made to a repository.

## Usage

To use the script, simply run `python main.py` in your terminal. The generated commit name will be printed to the console.

## Note

The script makes use of the `subprocess` module to run the `git diff` command, which retrieves a summary of the changes made to the repository. If there is an error when running this command (e.g. if `git` is not installed or if the current directory is not a git repository), an error message will be raised.
