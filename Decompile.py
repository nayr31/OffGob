import os

home = os.getcwd()

def write_raw(filename: str, output: list):
    with open(filename, "w+") as f:
        f.writelines(output)

def write_single_to_folder(foldername: str, filename: str, output: list):
    os.chdir(foldername)
    write_raw(filename, output)
    os.chdir("..")

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

meta_lines = []
location_lines = []
creature_lines = []
org_lines = []
quest_lines = []
things_lines = []
connections_lines = []
notes_lines = []
timeline_notes = []
blurb_notes = []

with open(notebook_name, "r") as file:
    print("Reading...")
    lines = file.readlines()

    record_mode = 0

    # This method takes care of empty categories
    def empty_format(st: str):
        return st.replace(" ", "").replace("[", "").replace("]", "")

    # Update the record mode depending on the newest line read
    def update_mode(x):
        if x == "locations:\n":
            return 1
        elif x == "creatures:\n":
            return 2
        elif x == "organisations:\n":
            return 3
        elif x == "quests:\n":
            return 4
        elif x == "things:\n":
            return 5
        elif x == "connections:\n":
            return 6
        elif x == "notes: []\n":
            return 7
        elif x == "timeline:\n":
            return 8
        elif x == "blurb: >-\n":
            return 9
        return -1

    # Add the line depending on the current record mode
    def add_line(x):
        if record_mode == 0:
            meta_lines.append(x)
        elif record_mode == 1:
            location_lines.append(x)
        elif record_mode == 2:
            creature_lines.append(x)
        elif record_mode == 3:
            org_lines.append(x)
        elif record_mode == 4:
            quest_lines.append(x)
        elif record_mode == 5:
            things_lines.append(x)
        elif record_mode == 6:
            connections_lines.append(x)
        elif record_mode == 7:
            notes_lines.append(x)
        elif record_mode == 8:
            timeline_notes.append(x)
        elif record_mode == 9:
            blurb_notes.append(x)

    # Read in file and sort the data
    for line in lines:
        upd = update_mode(empty_format(line))
        record_mode = upd if upd != -1 else record_mode
        add_line(line)

# Done reading
# Now we make the underlying folder and write some backup files
try:
    os.mkdir(notebook_name.split(".")[0])
except:
    # TODO Make this an input before release
    print("Seems this notebook exists. Merging isn't supported, so I'm gonna overwrite everything!")

# Move into the main folder
os.chdir(notebook_name.split(".")[0])

write_raw("meta.txt", meta_lines)
write_raw("blurb.md", blurb_notes)
try:
    os.mkdir("locations")
    os.mkdir("creatures")
    os.mkdir("organizations")
    os.mkdir("quests")
    os.mkdir("things")
except:
    # Folders were here already
    pass

# Write backup files
write_single_to_folder("locations", "original.back", location_lines)
write_single_to_folder("creatures", "original.back", creature_lines)
write_single_to_folder("organizations", "original.back", org_lines)
write_single_to_folder("quests", "original.back", quest_lines)
write_single_to_folder("things", "original.back", things_lines)
write_raw("connections.back", connections_lines)
write_raw("notes.back", notes_lines)

# Grab the name from the object, skipping nested objects
def grab_name(list: list):
    for line in list:
        if line[2:6] == "name":
            return line[8:-1]

# Removes the first two characters from each item in a list then returns the list
def remove_first_two_spaces(list: list):
    ret_list = []
    for lis in list:
        if len(lis) > 2 and (lis[0] == " " and lis[1] == " "):
            ret_list.append(lis[2:])
    return ret_list

def decompose_master(source_lines: list):

    # Record the encompassing objects that make up the file
    objects = []
    adding_object = []

    # For each line, we collect the "header" lines into a list
    for index, line in enumerate(source_lines):
        # If we hit a new object, add the old one to the list
        if line [0] == "-" and index != 1:
            objects.append(adding_object)
            adding_object = []

        # Don't add the first line, as it's just a header
        if index != 0:
            adding_object.append(line)
        
    # Add the last object
    if len(adding_object) > 0: # Don't add empty objects
        objects.append(adding_object)

    # For each item in the list, create a new folder if the object ends with "[]", then repeat the process on the folders created
    for obj in objects:
        if len(obj) > 0:
            name = grab_name(obj)
            # If the first line has "[]" at the end, it's a nested object and needs recursion
            if obj[0][-3:] != "[]\n": # (This is the nested object)
                # Create a folder for the object
                try:
                    os.mkdir(name)
                except:
                    # Folder already exists
                    pass

                # Move into the folder
                os.chdir(name)

                # Take the first line and last 16 lines and record them
                first_line = obj[0]
                last_16 = obj[-16:]

                # Combine them into a single list
                this_obj = [first_line] + last_16

                # Write the file
                write_raw("original.back", this_obj)

                # Remove the first line and last 16 lines from obj
                obj = remove_first_two_spaces(obj[1:-16])

                # Run this method again for obj
                decompose_master(obj)

                # Exit the folder
                os.chdir("..")

            # Otherwise we can just write the file in its own folder
            else: 
                # Create a folder for the object
                try:
                    os.mkdir(name)
                except:
                    # Folder already exists
                    pass
                # TODO Backup files for now, in the future we want to split the markdown file off into its own file
                write_single_to_folder(name, name + ".back", obj)

def do_a_decompose(name: str, lines: list):
    # Move into the folder
    os.chdir(name)

    # Decompose the file
    decompose_master(lines)

    # Exit the folder
    os.chdir("..")

print("Decomposing files...")

do_a_decompose("locations", location_lines)
do_a_decompose("creatures", creature_lines)
do_a_decompose("organizations", org_lines)
do_a_decompose("quests", quest_lines)
do_a_decompose("things", things_lines)

print("Done!")