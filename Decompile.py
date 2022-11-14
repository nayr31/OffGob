import os

home = os.getcwd()

#def write_meta():
#    with open

# Read in the file
print("Working in " + home)
print("Looking for notebook...")

tgns = []
for file in os.listdir():
    if file.split(".")[-1] == "tgn":
        tgns.append(file)

if len(tgns) == 0:
    input("Couldn't find any notebooks files (\".tgn\"). Make sure I am in the same folder.")
    exit()
elif len(tgns) > 1:
    input("Too many notebooks! I only support looking at one at a time.")
    exit()

notebook_name = tgns[0]
print("Found notebook: \"" + notebook_name.split(".")[0] + "\"")

with open(notebook_name, "r") as file:
    print("Reading...")
    lines = file.readlines()

    meta_lines = []
    location_lines = []
    creature_lines = []
    org_lines = []
    quest_lines = []
    things_lines = []
    connections_lines = []
    notes_lines = []
    timeline_notes = []

    record_mode = 0

    def choose_mode(x):
        if x == "locations\n":
            record_mode = 1
        elif x == "creatures\n":
            record_mode = 2
        elif x == "organisations:\n":
            record_mode = 3
        elif x == "quests:\n":
            record_mode = 4
        elif x == "things:\n":
            record_mode = 5
        elif x == "connections:\n":
            record_mode = 6

    for line in lines:
        choose_mode(line)




    try:
        os.mkdir(notebook_name.split(".")[0])
    except:
        #input("Seems like this notebook was exported already. I don't support merging yet (delete the folder).")
        #exit()
        pass

    # (Need to check for redundancy once we implement merging)

    # Move into the main folder
    os.chdir(notebook_name.split(".")[0])

