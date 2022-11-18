import os, yaml

# Given a folder for the notebook, recombine the yaml data
def combine_notebook(book: str):
    os.chdir(book)
    