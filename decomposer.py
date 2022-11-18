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
    
    notebook_name = book.strip(".tgn")

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

    def write_page(page: str):
        os.chdir(page)
        with open(page + " backup.yaml", "w") as f:
            f.writelines(yaml.dump(book_data[page]))
        os.chdir("..")

    def write_pages():
        for p in pages:
            write_page(p)

    write_pages()
    
    os.chdir("..")