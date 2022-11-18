# OffGob

[The Goblin Notebook](the-goblin.net) is an online-only website for notebook creation, and is a really good tool for it. However, sometimes one wants to have a local copy of their notebooks, and this is where OffGob comes in.

OffGob is a tool that allows you to convert your exported Goblin notebooks into a file structure separated by column and has support for any number of nested objects (limited by pythons recursion limit).

## Usage

Currently the project is limited to `.py` files. To use it, you need to have Python 3 installed on your machine and a little know-how in running their scripts.

### Steps:

1. Export your notebook from The Goblin Notebook.
2. Download this repository using the green button on the top right and extract it.
3. Place your `.tgn` file in the same folder as `offgob.py` so they can see each other.
4. Run `offgob.py` using Python 3 and choose your notebook.

## Features

- [x] Export `.tgn` files to a readable file structure.
- [x] Makes `.md` files of all objects in every category
- [ ] Combining
  - After modifying your notebook file structure, it will attempt to recombine the files back into an importable `.tgn` file
- [ ] Single object imports
  - Choose a markdown or text file (`.md`/`.txt`) and an object type and it will create an importable file for you
- [ ] Executable
  - A single `.exe` file that can be run on any Windows machine without the need for Python.
- [ ] Single object addition
  - Given a single object, it will add it to the notebook.
  - This may include both `.md` files and `.tgn` files.
- [ ] [Joplin](https://joplinapp.org/) support? 

## Known Issues/Side effects

Below is a list of known problems that may/may not being worked on. 

- Decomposing will fail if you have renamed your categories
- Has not been tested on notebooks with disabled categories