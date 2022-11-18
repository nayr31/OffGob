import os, time, tgnloader, decomposer

def decompose():
    print("Loading notebook data...")
    book = tgnloader.get_data()
    print("Using notebook: " + book)
    
    print("Running decomposer.py")
    decomposer.export(book)
    
    print("Finished decomposing notebook!\n")

# Wait for 1 second before exiting
def graceful_exit():
    print("Goodbye!")
    time.sleep(1)
    exit()

options = {
    "Exit": graceful_exit,
    "Decompose Notebook": decompose,
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
