# OffGob

[The Goblin Notebook](the-goblin.net) is an online-only website for notebook creation, and is a really good tool for it. However, sometimes one wants to have a local copy of their notebooks, and this is where OffGob comes in.

OffGob is a tool that allows you to convert your exported Goblin notebooks into a file structure separated by column and has support for any number of nested objects (limited by pythons recursion limit).

Note: Tested using the default Demo data from the Goblin website, there may be bugs.

## Usage

Currently the project is limited to `.py` files. To use it, you need to have Python 3 installed on your machine and a little know-how in running their scripts.

**Note**: This script was tested on a branch of Debian Linux, but should still work for Windows. MasOS is untested, and most likely will be unsupported for the time being.

### Export your notebook

To get your notebook campaign file, you'll need to:

1. Open [The Goblin Notebook](the-goblin.net).
2. Click on the cog.
3. Scroll down the pop-out and click the "export data" option.
4. Exporting your campaign will download it as a `.tgn` file.

**Note:** The Goblin Notebook is still in development, so the above instructions may be inaccurate.

### Decompile your notebook

1. Make sure your campaign `.tgn` file in the same folder as `offgob.py` so they can see each other.
2. Run `offgob.py` using Python 3 and choose the "Decompile Notebook" option.

### Compile your notebook

**Note:** This only works with notebooks that were exported using OffGob, and currently only supports adding 1 more depth to categories.

1. Run `offgob.py` using Python 3 and choose the "Combine Notebook" option.
2. You'll find the compiled notebook in the same folder as `offgob.py` with the name `[notebook name]-export.tgn`.

### Convert a markdown file to an importable object

1. Place your file inside the `_markdown` folder.
2. Run `offgob.py` using Python 3 and choose the  "Convert markdown to tgn" option.
3. If you have more than one file, it will prompt you to choose one.
4. Select a template to use depending on the type of object.

**Note**: The templates are located in the `_templates` folder. You can add your own templates there, but I wouldn't recommend it.

### Bulk convert into a single file

1. Create a folder inside of the `_markdown` folder (for example, "Spells").
2. Place your desired `.md` files inside that newly created folder.
3. Run `offgob.py` using Python 3 and choose the  "Bulk convert markdown to tgn" option.
4. It may prompt you to select a folder if you've created more than one.
5. Select the type of object that the files are using the templates (ie. which column it goes into).

## Features (extended)

Below is a list of features that are currently implemented in OffGob, or are planned.

- [x] Exporting (decomposing) notebooks
  - [x] Export `.tgn` files to a readable file structure.
  - [x] Makes `.md` files of all objects in every category
  - [x] Record some specific metadata per object
- [x] Combining
  - [x] Select a notebook folder and recompile it back into a `.tgn` file, creating some metadata files.
  - [x] Supports importing non-native objects (such as items that were added manually).
- [x] Object imports
  - [x] Choose a markdown or text file (`.md`/`.txt`) and an object type and it will create an importable file for you
  - [x] Create a single file that contains multiple objects from a single column
- [ ] Executable
  - A single `.exe` file that can be run on any Windows machine without the need for Python. This is planned for a final release, as it increases release and testing time.

## Known Issues/Side effects

Below is a list of known problems that may/may not being worked on.

- Decomposing will fail if you have renamed your categories
- Has not been tested on notebooks with disabled categories
- There is an incredibly small chance that the created object id matches with a pre-existing object, which may cause problems.
- Fails to add objects that were manually added that are considered more than 1 deeper than it had originally
- White squares show up after importing, but go away after refreshing. This could be a tagging issue and are not supported.

## Help

If you have any questions regarding how to use the program or if you found a bug, you can contact me through the [Goblin Discord](https://discord.gg/C56sTY6fd4) @gamernayr#8165. I'm usually online there, and I'll be happy to help you out. Do not DM me.

### Running the script

I'll include this here for people who are new to programming or may have trouble running the script.

**Note**: These steps assume you are using Windows or Linux. I have no idea how to run Python scripts on Macs or other operating systems such as Android or iOS.

1. Download the repository using the green button on the top right of the page and extract it to a folder.
2. Download and install Python 3 from [here](https://www.python.org/downloads/).
3. Download and install VSCode from [here](https://code.visualstudio.com/).
4. Install the python extension for VSCode using the extensions tab on the left.
5. Restart VSCode.
6. In VSCode, open the folder where you extracted the repository using `File > Open Folder...`.
7. Click on `offgob.py` in the explorer tab on the left.
8. Run the script using the arrow in the top right corner of the window.
9. Follow the prompts in the terminal at the bottom of the window.

The program may fail to start, as there may be some custom scripts that are not included in the repository. If this happens, you can contact me on the Goblin Discord and I'll update this guide on how to fix it.

## Video Demonstration

Below is a video showing how you can create and edit new items within your file structure (doesn't have to be through VSCode) and recompile them back into the Goblin Notebook.

[OffGob Demo.webm](https://user-images.githubusercontent.com/69859977/202892596-3318918e-77f4-4af5-8716-9d865e4bdc89.webm)
