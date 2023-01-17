# This file handles everything to do with the templates
# It is required since 

import os, yaml

global templates
templates = None
global names
names = []

def load_template_data() -> dict:
    os.chdir("_templates")
    # Fill template list
    templates = {}
    for file in os.listdir():
        if file.endswith(".yaml"):
            with open(file, "r") as f:
                template_name = file.split(".")[0]
                names.append(template_name)
                templates[template_name] = yaml.load(f, Loader=yaml.FullLoader)
    
    os.chdir("..")
    return templates

def get_template_by_name(name: str) -> dict:
    #if templates is None:
    #    load_template_data()
    
    if name in templates:
        return templates[name]
    else:
        return None
    
def choose_template():
    name = None
    while True:
        print("Available Templates:")
        for index, template in enumerate(templates):
            print("{0} - {1}".format(index, template))
        choice = input("Enter the number of the template you want to use: ")
        if choice.isdigit():
            if int(choice) in range(len(names)):
                name = names[int(choice)]
                return get_template_by_name(name), name
            else:
                print("That number is not in the list!")
        else:
            print("That is not a number!")

if templates == None:
    print("Loading templates...")
    templates = load_template_data()