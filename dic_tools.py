def get_nth_key(dictionary, n=0, both=False):
    if n < 0:
        n += len(dictionary)
    for i, value in enumerate(dictionary.values()):
        if i == n:
            if both:
                return value
            return value
    raise IndexError("dictionary index out of range") 

def list_choose(list: list, noun: str):
    while True:
        for index, innoun in enumerate(list):
            print("{0} - {1}".format(index, innoun))
        choice = input("Enter the number of the " + noun + " you want to use: ")
        if choice.isdigit():
            if int(choice) in range(len(list)):
                return list[int(choice)]
            else:
                print("That number is not in the list!")
        else:
            print("That is not a number!")

def dict_choose(dictionary: dict, does_break=True, executes=True):
    while True:
        # Print the options
        for index, option in enumerate(dictionary):
            print(f"[{index}] {option}")
        x = input("Input the number of the option you want to use: ")
        if x.isdigit():
            # If we found a valid response, run the function
            if executes:
                get_nth_key(dictionary, int(x))()
            else:
                return get_nth_key(dictionary, int(x))
            if does_break:
                break
        else:
            print("That is not a number!")