import os, yaml, random, string
import templater

# Given a folder for the notebook, recombine the yaml data
def combine_notebook(book: str):
    pages = ["locations", "creatures", "organisations", "quests", "things"]

    os.chdir(book)
    
    def get_yaml_data(name: str, nester: str):
        # Check if the folder is empty
        items_in_folder = os.listdir()
        if len(items_in_folder) == 0:
            print("Folder is empty: " + name + " I'm sorry!")
            return None
        
        # See if there's a blurb file
        blurb = None
        try:
            with open("blurb.md", "r") as f:
                blurb = f.read()
        except:
            print("No blurb file found for " + name + " I'm sorry!")
            return None
        
       # Get the data from the backup file
        data = None
        
        # Manually created items should have their backups created
        if name + "_backup.yaml" not in items_in_folder:
            print("No backup file found for " + name + " I'll try to make it!")
            # There is a markdown, meaning that we need to create the backup file
            template = templater.get_template_by_name(str.capitalize(nester))
            data = template[nester][0]
            # Fill out the information
            data["blurb"] = blurb
            data["name"] = name
            data["id"] = "".join(random.choices(string.ascii_letters + string.digits, k=16))
            with open(name + "_backup.yaml", "w") as f:
                f.write(yaml.dump(data))
        else: # Otherwise we just load the data to update the blurb
            with open(name + "_backup.yaml", "r") as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                data["blurb"] = blurb
        
        # Check if there are any nested objects
        for item in os.listdir():
            if os.path.isdir(item):
                # If there are, do this function again
                os.chdir(item)
                gotten_data = get_yaml_data(item, nester)
                if gotten_data != None:
                    data[nester].append(gotten_data)
                os.chdir("..")
            
        return data
    
    #try:
    notebook_data = yaml.load(open(book + ".yaml", "r"), Loader=yaml.FullLoader)
    
    # For each page, load the data and add it to the notebook data
    for page in pages:
        os.chdir(page)
        
        # Empty the data in the main data file
        # It's just a list of the objects anyway, no metadata
        notebook_data[page] = []
        
        for item in os.listdir():
            # For each object in the page, load it's data and add it 
            if os.path.isdir(item):
                os.chdir(item)
                notebook_data[page].append(get_yaml_data(item, page))
                os.chdir("..")
        os.chdir("..")
        
    # Write the notebook data to a file
    with open(book + "-export.tgn", "w") as f:
        f.write(yaml.dump(notebook_data))
    
    os.chdir("..")
    
    return True, None