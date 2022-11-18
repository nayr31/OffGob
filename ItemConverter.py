import random, os

# TODO Support the other types of things

try:
    os.mkdir("Items")
except:
    pass
os.chdir("Items")

print("Make sure the item(s) you want to convert is inside the Items folder as `.md` files.")
input("Press enter to continue...")

# Make a list of all files that end in ".md"
for item in os.listdir():
    if item.endswith(".md"):
        # Open the file
        with open(item, "r") as f:
            lines = f.readlines()
        
