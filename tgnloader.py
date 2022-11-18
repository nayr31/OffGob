import os, yaml

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

def get_data():
    tgns = []
    for file in os.listdir():
        if file.split(".")[-1] == "tgn":
            tgns.append(file)

    if len(tgns) == 0:
        input("Couldn't find any notebooks files (\".tgn\"). Make sure I am in the same folder as them!")
        exit()
    elif len(tgns) == 1:
        return tgns[0]
    else:
        return ask_for_notebook(tgns)
        
# Given a filename, open a notebook and return the data
def open_notebook(filename: str):
    with open(filename, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data