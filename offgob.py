import os, time, random, string, yaml, copy
import tgnloader, decomposer, combiner, omni, dic_tools, templater


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

# Creates an object file from a markdown file
def convert_md_to_tgn():
    print("I am about to look inside of the \"_markdown\" folder for a [.md] or [.txt] file.")

    # Get the markdown file
    os.chdir("_markdown")
    md_file = omni.find_markdown()
    os.chdir("..")
    
    if md_file is None:
        print("Failed to find a markdown file, I'm sorry!\n")
        return
    print("Using markdown file: " + md_file)
    
    # Choose a template
    chosen_template, template_name = templater.choose_template()
    template_name = str.lower(template_name)

    # Using the template dictionary, create a new file with modified values based on the markdown file
    chosen_template[template_name][0]["blurb"] = open("_markdown/" + md_file, "r").read()
    chosen_template[template_name][0]["name"] = md_file[:-3]
    chosen_template[template_name][0]["id"] = ''.join(random.choices(string.ascii_lowercase, k=10))

    #capsule = {str.lower(template_name): chosen_template}
    
    os.chdir("_tgn_special")
    with open(md_file[:-3] + ".tgn", "w") as f:
        f.write(yaml.dump(chosen_template))
    os.chdir("..")
    
    print("Done creating object! You'll find it in the \"tgn_special\" folder.\n")
    return

def convert_bulk_md_to_tgn():
    print("I am about to look inside of the \"_markdown\" folder for another folder.")

    folders = []

    os.chdir("_markdown")
    for folder in  os.listdir():
        if os.path.isdir(folder):
            folders.append(folder)
    os.chdir("..")

    chosen_folder = None

    if len(folders) == 0:
        print("I couldn't find any folders!")
    elif len(folders) == 1:
        chosen_folder = folders[0]
        print("Using " + chosen_folder + " as folder target.")
    else:
        chosen_folder = dic_tools.list_choose(folders, "folder")

    print("Loading markdown files...")
    os.chdir("_markdown")
    os.chdir(chosen_folder)
    working = os.getcwd()
    md_files = omni.load_markdown()
    os.chdir("..")
    os.chdir("..")

    print("Got {0} items!".format(len(md_files)))

    # Choose a template
    chosen_template, template_name = templater.choose_template()
    template_name = str.lower(template_name)

    os.chdir("_tgn_special")
    #try:
    #    os.mkdir(chosen_folder)
    #except:
    #    pass
    #os.chdir(chosen_folder)

    #contained = None
    #pick = input("Do you want the objects contained into their own object? (y/n)")
    #while True:
    #    if pick == "y":
    #        contained = True
    #        break
    #    elif pick == "n":
    #        contained = False
    #        break
    #    else:
    #        print("Please type either \'y\' or \'n\' (Got " + input + ").")

    items = []

    #if contained:
    #    items = copy.deepcopy(chosen_template)
    #    items["name"] = chosen_folder
    #    items["blurb"] = ""
    #    items["id"] = ''.join(random.choices(string.ascii_lowercase, k=10))
        

    for md_file in md_files:
        # Using the template dictionary, create a new file with modified values based on the markdown file
        chosen_template[template_name][0]["blurb"] = open(os.path.join(working, md_file), "r").read()
        chosen_template[template_name][0]["name"] = md_file[:-3]
        chosen_template[template_name][0]["id"] = ''.join(random.choices(string.ascii_lowercase, k=10))

        #if contained:
        #    items[template_name][0][template_name].append(copy.deepcopy(chosen_template[template_name][0]))
        #else:
            
        items.append(copy.deepcopy(chosen_template[template_name][0]))

        # Writes out each item one by one currently
        #with open(md_file[:-3] + ".tgn", "w") as f:
        #    f.write(yaml.dump(chosen_template))

    with open(chosen_folder + ".tgn", "w") as f:
        f.write(template_name + ":\n")
        f.write(yaml.dump(items))

    #os.chdir("..") # Break chosen folder
    os.chdir("..") # Break _tgn_special
    
    print("Done bulk exporting! You'll find a bulk import file in the \"_tgn_special\" folder.\n")

options = {
    "Exit": graceful_exit,
    "Decompose Notebook": decompose,
    "Combine Notebook": combine,
    "Convert markdown to tgn" : convert_md_to_tgn,
    "Bulk convert markdown to tgn": convert_bulk_md_to_tgn,
} 

# Select an option from the options dictionary
print("Welcome to the OffGob!\n")

# Print the options to the user until they want to exit
dic_tools.dict_choose(options, does_break=False)
