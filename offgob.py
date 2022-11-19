import os, time, tgnloader, decomposer, combiner, yaml

def decompose():
    print("Loading notebook data...")
    book = tgnloader.get_notebook_filename()
    if book is None:
        print("Failed to find a notebook file, I'm sorry!\n")
        return
    print("Using notebook: " + book)
    
    print("Running decomposer.py")
    decomposer.export(book)
    
    print("Finished decomposing notebook!\n")

def combine():
    print("Looking for existing notebooks...")
    
    existing_book_folder = tgnloader.ask_for_existing()
    if existing_book_folder is None:
        print("Failed to find an existing notebook, I'm sorry!\n")
        return
    
    print("Attempting to combine notebook: " + existing_book_folder)
    done_good = combiner.combine_notebook(existing_book_folder)
    
    if done_good:
        print("Finished combining notebook!\n")
    else:
        print("Failed to combine notebook!\n")
    
# Wait for 1 second before exiting
def graceful_exit():
    print("Goodbye!")
    time.sleep(1)
    exit()

options = {
    "Exit": graceful_exit,
    "Decompose Notebook": decompose,
    "Combine Notebook": combine,
}

def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, value in enumerate(dictionary.values()):
        if i == n:
            return value
    raise IndexError("dictionary index out of range") 

# Select an option from the options dictionary
print("Welcome to the OffGob!\n")

while True:
    # Print the options
    for index, option in enumerate(options):
        print(f"[{index}] {option}")
    x = input("Input the number of the option you want to use: ")
    if x.isdigit():
        get_nth_key(options, int(x))()
    else:
        print("That is not a number!")
