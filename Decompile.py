import os

home = os.getcwd()

def write_raw(filename: str, output: list):
    with open(filename, "w+") as f:
        f.writelines(output)

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
    blurb_notes = []

    record_mode = 0

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
        upd = update_mode(line)
        record_mode = upd if upd != -1 else record_mode
        add_line(line)

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
