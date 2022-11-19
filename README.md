# OffGob

[The Goblin Notebook](the-goblin.net) is an online-only website for notebook creation, and is a really good tool for it. However, sometimes one wants to have a local copy of their notebooks, and this is where OffGob comes in.

OffGob is a tool that allows you to convert your exported Goblin notebooks into a file structure separated by column and has support for any number of nested objects (limited by pythons recursion limit).

Note: Tested using the default Demo data from the Goblin website, there may be bugs.

## Usage

Currently the project is limited to `.py` files. To use it, you need to have Python 3 installed on your machine and a little know-how in running their scripts.

### Steps:

1. Download this repository using the green button on the top right of the page and extract it.
2. Run `python3 offgob.py` in the directory you extracted the repository to.

#### Export your notebook

1. Export your notebook from The Goblin Notebook.
2. Place your `.tgn` file in the same folder as `offgob.py` so they can see each other.
3. Run `offgob.py` using Python 3 and choose the "Decompile Notebook" option.

#### Compile your notebook

Note: This only works with notebooks that were exported using OffGob.

1. Run `offgob.py` using Python 3 and choose the "Combine Notebook" option.
2. You'll find the compiled notebook in the same folder as `offgob.py` with the name `[notebook name]-export.tgn`.

#### Create an importable thing

1. Run `offgob.py` using Python 3 and choose the "Omni-tool" option.
2. Choose the "Convert markdown to tgn" option.
3. 

## Features (extended)

Below is a list of features that are currently implemented in OffGob, or are planned.

- [x] Exporting (decomposing) notebooks
  - [x] Export `.tgn` files to a readable file structure.
  - [x] Makes `.md` files of all objects in every category
  - [x] Record some specific metadata per object
- [ ] Combining
  - [x] Select a notebook folder and recompile it back into a `.tgn` file, given there are the required metadata files.
  - [ ] Given a single `.md` or `.tgn` file, import it into a notebook.
- [ ] Single object imports
  - Choose a markdown or text file (`.md`/`.txt`) and an object type and it will create an importable file for you
- [ ] Executable
  - A single `.exe` file that can be run on any Windows machine without the need for Python.
- [ ] Object creator/editor/destructor
  - [ ] Using the interface, choose a category and add an object to it depending on some user defined variables Supports all object types, and placing them inside other objects.
  - [ ] Choose an object and edit it's metadata.
  - [ ] Choose and object to delete it.
- [ ] [Joplin](https://joplinapp.org/) support? 

## Known Issues/Side effects

Below is a list of known problems that may/may not being worked on. 

- Decomposing will fail if you have renamed your categories
- Has not been tested on notebooks with disabled categories
- There is an incredibly small chance that the created object id matches with a pre-existing object is, which may cause problems.

## Help

If you have any questions regarding how to use the program or if you found a bug, you can contact me through the [Goblin Discord](https://discord.gg/8Z7Y4Z).

If you've never used Python before, I'd recommend you download [Visual Studio Code](https://code.visualstudio.com/) and install the Python extension. This will allow you to run the script from within the editor using a little play button in the top right corner. Just make sure to open the **folder** containing the script and not the script itself.