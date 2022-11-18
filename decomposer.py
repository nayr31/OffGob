import os, tgnloader, yaml

def export(book):
    pages = ["locations", "creatures", "organisations", "quests", "things"]
    
    errors = []
    try:
        book_data = tgnloader.open_notebook(book)
        print("Loaded notebook data successfully")
    except:
        input("Failed to load notebook data, I'm sorry!")
        exit()
    
    
    notebook_name = book[:-4]
    print("You can find the decomposed notebook in the folder: " + notebook_name)

    # Given a string, return the data for that page in book_data
    def print_page(page: str):
        print(page + "\n" + str(book_data[str.lower(page)]))

    # Given a string, create a folder with that name
    def make_dir(path: str):
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            errors.append("Directory already exists: " + path)

    # Create a folder for the notebook and move into it
    make_dir(notebook_name)
    os.chdir(notebook_name)

    # Create a folder for each page in the notebook
    make_dir("locations")
    make_dir("creatures")
    make_dir("quests")
    make_dir("organisations")
    make_dir("things")
    
    def write_objects(data, nester: str):
        # Find the name inside the yaml data
        object_name = data["name"]
        make_dir(object_name)
        os.chdir(object_name)
        
        # Write a markdown file for the object of whatever is inside the "blurb"
        with open("blurb.md", "w") as f:
            f.write(data["blurb"])
        
        # If there are objects nested inside, do this function again
        if len(data[nester]) > 0:
            for obj in data[nester]:
                write_objects(obj, nester)
            
        os.chdir("..")
    
    # Given a string, dump the corresponding data to a file
    def write_page(page: str):
        os.chdir(page)
        # Create the backup file
        with open(page + " backup.yaml", "w") as f:
            f.writelines(yaml.dump(book_data[page]))
        
        # Double make sure that the data loads correctly
        with open(page + " backup.yaml", "r") as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            # After loading the data, we have a list of the different parent objects
            # We need to preform write_objects on each of them
            for object in data:
                write_objects(object, page)
        
        os.chdir("..")

    # For each of the pages, write the backup data to a file
    for p in pages:
        write_page(p)

    os.chdir("..")