import os, copy

home = os.getcwd()

errors = []

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
write_raw("connections.back", connections_lines)
write_raw("notes.back", notes_lines)

# Grab the name from the object, skipping nested objects
def grab_name(list: list):
    for line in list:
        if line[2:6] == "name":
            return line[8:-1]
    errors.append("Couldn't find a name for an object!\n" + str(list))
    return "ERROR"

# Removes the first two characters from each item in a list then returns the list
def remove_first_two_spaces(list: list):
    ret_list = []
    for lis in list:
        if len(lis) > 2 and (lis[0] == " " and lis[1] == " "):
            ret_list.append(lis[2:])
    return ret_list
    
# Working backwards in a list, return the index of the first line that starts with "-"
def find_start_of_object(lines: list):
    for i in range(len(lines) - 1, -1, -1):
        if lines[i][0] == "-":
            return i
    print("ERROR: Couldn't find the start of an object! This is a bug, please report it.")
    return 0

# Given a list of lines, return the last line that starts with a given string
def find_end_of_object(lines: list, delimiter: str):
    for i in range(len(lines) - 1, 0, -1):
        if delimiter in lines[i]:
            return i
    print("ERROR: Couldn't find the end of an object! This is a bug, please report it.")
    return len(lines)

def decompose_master(source_lines: list, delimiter: str):
    
    # This shouldn't happen, but just in case
    if len(source_lines) == 0:
        print("Empty list passed to decompose_master")
        return
    elif len(source_lines) == 1:
        print("ERROR: Skipped a header?")
        return
    
    new_lines = copy.deepcopy(source_lines)
    
    while len(new_lines) > 1:
        # Find the start of the bottom-most object
        start = find_start_of_object(new_lines)
        end = len(new_lines)
        
        is_nested = False
        
        # Check if the object is nested
        if new_lines[start][-3:] != "[]\n":
            is_nested = True
        
        # If it is, then we need to find the end of the object inside it
        if is_nested:
            end = find_end_of_object(new_lines[start:], delimiter) + start
            #start += 1
        
        #trimmed_lines = new_lines[start:end]
        
        # Grab the object, nested or not
        #new_obj = remove_first_two_spaces(new_lines[start:end])
        new_obj = new_lines[start:end]
        
        if is_nested:
            new_obj = remove_first_two_spaces(new_obj)

        # Remove the object we just extracted from the list
        new_lines = new_lines[:start] + new_lines[end:]
        
        # Grab the name of the new_obj then write it to a file 
        name = grab_name(new_obj)
        try:
            os.mkdir(name)
        except:
            # Folder was here already
            pass
        os.chdir(name)
        write_raw("original.back", new_obj)
        
        # new_obj needs to either be written to a file or passed back to this function
        if is_nested:
            decompose_master(new_obj, delimiter)
        else:
            pass
        
        # Go back
        os.chdir("..")
            
        
# Decompose the master files into their own folders
# These will only happen on the outermost level (creatures, locations, etc)
def do_a_decompose(name: str, lines: list, delimiter: str):
    # Create the folder
    try:
        os.mkdir(name)
    except:
        # Folder already exists
        pass
    
    # Move into the folder
    os.chdir(name)
    
    # Create backup file
    write_raw("original.back", lines)

    # Decompose the file
    decompose_master(lines, delimiter)

    # Exit the folder
    os.chdir("..")

print("Decomposing files...")

#do_a_decompose("locations", location_lines, "subtype:")
#do_a_decompose("creatures", creature_lines, "statblock:")
#do_a_decompose("organizations", org_lines, "subtype:")
do_a_decompose("quests", quest_lines[1:], "subtype:")
#do_a_decompose("things", things_lines, "subtype:")

print("Done!")

if len(errors) > 0:
    print("Errors:")
    for error in errors:
        print(error)