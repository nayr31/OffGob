import os, yaml
import dic_tools

def find_markdown():
    md_files = []
    for file in os.listdir():
        if file.split(".")[-1] == "md":
            md_files.append(file)
    
    if len(md_files) == 0:
        return None
    elif len(md_files) == 1:
        return md_files[0]
    else:
        return dic_tools.list_choose(md_files, "markdown file")
    

def load_template():
    # Fill template list
    templates = {}
    template_name = ""
    for file in os.listdir():
        if file.endswith(".yaml"):
            with open(file, "r") as f:
                template_name = file.split(".")[0]
                templates[template_name] = yaml.load(f, Loader=yaml.FullLoader)
    
    #for template in templates:
    #    print("[" + str(list(templates.keys()).index(template)) + "] " + template)
    
    template = dic_tools.dict_choose(templates, executes=False)
    
    if template is None:
        return None
    else:
        return template, str.lower(template_name)
    
    # Load the template file from a user prompt
    while True:
        choice = input("Enter the number of the template you want to use: ")
        if choice.isdigit():
            if int(choice) in range(len(templates)):
                return list(templates.values())[int(choice)]
            else:
                print("That number is not in the list!")
        else:
            print("That is not a number!")
    