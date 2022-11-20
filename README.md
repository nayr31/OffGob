# OffGob

[The Goblin Notebook](the-goblin.net) is an online-only website for notebook creation, and is a really good tool for it. However, sometimes one wants to have a local copy of their notebooks, and this is where OffGob comes in.

OffGob is a tool that allows you to convert your exported Goblin notebooks into a file structure separated by column and has support for any number of nested objects (limited by pythons recursion limit).

Note: Tested using the default Demo data from the Goblin website, there may be bugs.

## Usage

Currently the project is limited to `.py` files. To use it, you need to have Python 3 installed on your machine and a little know-how in running their scripts.

**Note**: This script was tested on a branch of Debian Linux, but should still work for Windows. MasOS is untested, and most likely will be unsupported for the time being.

### Export your notebook

1. Export your notebook from The Goblin Notebook.
2. Place your `.tgn` file in the same folder as `offgob.py` so they can see each other.
3. Run `offgob.py` using Python 3 and choose the "Decompile Notebook" option.

### Compile your notebook

Note: This only works with notebooks that were exported using OffGob.

1. Run `offgob.py` using Python 3 and choose the "Combine Notebook" option.
2. You'll find the compiled notebook in the same folder as `offgob.py` with the name `[notebook name]-export.tgn`.

### Create an importable thing

1. Run `offgob.py` using Python 3 and choose the  "Convert markdown to tgn" option.
2. It will prompt you to place your file inside the `_markdown` folder.
3. Press enter. If you have more than one file, it will prompt you to choose one.
4. Select a template to use.

**Note**: The templates are located in the `_templates` folder. You can add your own templates there, but I wouldn't recommend it.

## Features (extended)

Below is a list of features that are currently implemented in OffGob, or are planned.

- [x] Exporting (decomposing) notebooks
  - [x] Export `.tgn` files to a readable file structure.
  - [x] Makes `.md` files of all objects in every category
  - [x] Record some specific metadata per object
- [x] Combining
  - [x] Select a notebook folder and recompile it back into a `.tgn` file, creating some metadata files.
  - [x] Supports importing non-native objects (such as items that were added manually).
- [ ] Single object imports
  - [x] Choose a markdown or text file (`.md`/`.txt`) and an object type and it will create an importable file for you
  - [ ] Given a `.tgn` file, import it into a chosen notebook (either in the file structure, or the parent `.tgn`).
- [ ] Object editor/destructor
  - [ ] Choose an object and edit it's metadata. 
  - [ ] Choose and object to delete it.
- [ ] Executable
  - A single `.exe` file that can be run on any Windows machine without the need for Python. This is planned for a final release, as it increases release and testing time.

## Known Issues/Side effects

Below is a list of known problems that may/may not being worked on. 

- Decomposing will fail if you have renamed your categories
- Has not been tested on notebooks with disabled categories
- There is an incredibly small chance that the created object id matches with a pre-existing object, which may cause problems.

## Help

If you have any questions regarding how to use the program or if you found a bug, you can contact me through the [Goblin Discord](https://discord.gg/C56sTY6fd4). I'm usually online there, and I'll be happy to help you out.

### Running the script

I'll include this here for people who are new to programming or may have trouble running the script.

**Note**: These steps assume you are using Windows or Linux. I have no idea how to run Python scripts on Macs or other operating systems such as Android or iOS.

1. Download the repository using the green button on the top right of the page and extract it to a folder.
2. Download and install Python 3 from [here](https://www.python.org/downloads/).
3. Download VSCode from [here](https://code.visualstudio.com/).
4. Install the python extension for VSCode using the extensions tab on the left.
5. Restart VSCode.
6. In VSCOde, open the folder where you extracted the repository using `File > Open Folder...`.
7. Click on `offgob.py` in the explorer tab on the left.
8. Run the script using the arrow in the top right corner of the window.
9. Follow the prompts in the terminal at the bottom of the window.

The program may fail to start, as there may be some custom scripts that are not included in the repository. If this happens, you can contact me on the Goblin Discord and I'll update this guide on how to fix it.

## Video Demonstration

Below is a video showing how you can create and edit new items within your file structure (doesn't have to be through VSCode) and recompile them back into the Goblin Notebook.

**Note**: The white squares after import go away after refreshing the page.

[OffGob Demo.webm](https://user-images.githubusercontent.com/69859977/202892596-3318918e-77f4-4af5-8716-9d865e4bdc89.webm)

