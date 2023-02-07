import os, yaml
import dic_tools

def ask_for_notebook(books: list):
    # Print the list of notebooks and ask which one to use
    print("Which notebook do you want to use?")
    for book in books:
        print("[" + str(books.index(book)) + "] " + book.split(".")[0])
    
    while True:
        choice = input("Enter the number of the notebook you want to use: ")
        if choice.isdigit():
            if int(choice) in range(len(books)):
                return books[int(choice)]
            else:
                print("That number is not in the list!")
        else:
            print("That is not a number!")

# Return a list of all folders and ask which one to use
def ask_for_existing():
    folders = []
    for item in os.listdir():
        if os.path.isdir(item) and item[0] != "." and item[0] != "_":
            folders.append(item)
    
    if len(folders) == 0:
        print("No valid folders found!")
        return None
    elif len(folders) == 1:
        return folders[0]
    else:
        print("Which folder do you want to use?")
        for folder in folders:
            print("[" + str(folders.index(folder)) + "] " + folder)
        
        return dic_tools.list_choose(folders, "folder")

# Returns the desired name of the notebook
def get_notebook_filename() -> str:
    tgns = []
    for file in os.listdir():
        if file.split(".")[-1] == "tgn":
            tgns.append(file)

    if len(tgns) == 0:
        print("Couldn't find any notebooks files (\".tgn\"). Make sure I am in the same folder as them!")
        return None
    elif len(tgns) == 1:
        return tgns[0]
    else:
        return ask_for_notebook(tgns)

def remove_tabs(filename: str):
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()
    new_lines = []
    for line in lines:
        new_lines.append(line.replace("\t", ""))
    with open ("safe_" + filename, "w") as f:
        f.writelines(new_lines)
        

# Given a filename, open a notebook and return the data
def open_notebook(filename: str):
    try:
        with open(filename, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data
    except:
        print("Found a problem loading the notebook, attempting to fix and try again.")
        remove_tabs(filename)
        data = None
        with open("safe_" + filename, "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
        os.remove("safe_" + filename)
        return data