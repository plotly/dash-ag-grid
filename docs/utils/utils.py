import os
from pathlib import Path
from importlib import import_module
from inspect import getsource
from fnmatch import fnmatch
import re
import plotly.express as px
import dash


EXAMPLE_APPS_DIR_NAME = "examples"
ROOT_DIR = Path(__file__).parent.parent
EXAMPLE_APPS_DIR = os.path.join(ROOT_DIR, EXAMPLE_APPS_DIR_NAME)
APP_ASSETS_DIR = os.path.join(ROOT_DIR, "assets")
app_description = """
Our documentation will help you to get up and running with AG Grid in your Dash app
"""


def file_names():
    walk_dir = EXAMPLE_APPS_DIR
    names = []
    module_names = []

    for (root, dirs, files) in os.walk(walk_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".") and not d.startswith("_")]
        for file in files:
            if file.startswith("_") or file.startswith(".") or not file.endswith(".py"):
                continue
            file = file.replace(".py", "")
            if file in names:
                raise Exception(
                    f"filenames must be unique.  `{file}.py` already exists"
                )
            names.append(file)

            example_filename = os.path.join(root, file).replace("\\", "/")
            _, _, example_filename = example_filename.partition(
                walk_dir.replace("\\", "/") + "/"
            )
            example_filename = example_filename.replace(".py", "").replace("/", ".")

            example_folder = (
                EXAMPLE_APPS_DIR_NAME.replace("\\", "/").lstrip("/").replace("/", ".")
            )

            module_name = ".".join([example_folder, example_filename])
            module_names.append(module_name)
    return names, module_names


#
# def file_names():
#     names = []
#     for filename in os.listdir(EXAMPLE_APPS_DIR):
#         print("filename", filename)
#         if not filename.startswith("_") and filename.endswith(".py"):
#             filename = filename.replace(".py", "")
#             if filename in names:
#                 raise Exception(
#                     f"filenames must be unique.  `{filename}.py` already exists"
#                 )
#             names.append(filename)
#     return names


file_names, module_names = file_names()
example_modules = {p: import_module(p) for p in module_names}
example_apps = {p: m.app for p, m in example_modules.items()}
example_source_codes = {p: getsource(m) for p, m in example_modules.items()}


def file_name_from_path(path):
    for page in dash.page_registry.values():
        template = page.get("path_template")
        if template:
            # check that static sections of the pathname match the template
            wildcard_pattern = re.sub("<.*?>", "*", template)
            if fnmatch(path, wildcard_pattern):
                return page["module"].split(".")[-1]
        if page["relative_path"] == path:
            return page["module"].split(".")[-1]
    return ""


def search_code_files(
    searchterms, case_sensitive, search_type="and", include_description=True
):
    """
    returns a list of filenames of the example apps that contain the search terms

    Note:  The file names of the example apps must be unique, even if they are in subdirectories.  This will make it
           possible to match the example app file name with the correct page in the dash.page_registry, even if the
           file structure for two are different.

    """

    searchterms = searchterms.split()
    if not case_sensitive:
        searchterms = [terms.lower() for terms in searchterms]

    # initialize the index of filenames of code with the search terms
    index = {term: set() for term in searchterms}

    for filename, code in example_source_codes.items():
        if include_description:
            module = "pages." + filename
            app_description = dash.page_registry[module]["description"]
            code = "\n".join([app_description, code])

        if not case_sensitive:
            code = code.lower()

        # build index of filenames of code with the search terms
        for term in searchterms:
            if term in code:
                index[term].add(filename)

    search_results = [index.get(term, set()) for term in searchterms]

    if search_type == "and":
        return set.intersection(*search_results)
    # search_type is "or"
    return set.union(*search_results)


def filter_registry(
    searchterms, case_sensitive, search_type="and", include_description=True
):
    """
    Returns a filtered dash.page_registry dict based on a list of example app names
    """

    filtered_example_app_list = search_code_files(searchterms, case_sensitive)

    # We use the module param to filter the dash_page_registry
    # Note that the module name includes the pages folder name eg: "pages.bar-charts"
    filtered_registry = []
    for page in dash.page_registry.values():
        filename = page["module"].split("pages.")[1]
        if filename in filtered_example_app_list:
            filtered_registry.append(page)
    return filtered_registry


plotly_template = [
    "bootstrap",
    "plotly",
    "ggplot2",
    "seaborn",
    "simple_white",
    "plotly_white",
    "plotly_dark",
    "presentation",
    "xgridoff",
    "ygridoff",
    "gridon",
    "none",
]

continuous_colors = px.colors.named_colorscales()

discrete_colors = {
    "Plotly": px.colors.qualitative.Plotly,
    "D3": px.colors.qualitative.D3,
    "G10": px.colors.qualitative.G10,
    "T10": px.colors.qualitative.T10,
    "Alphabet": px.colors.qualitative.Alphabet,
    "Dark24": px.colors.qualitative.Dark24,
    "Light24": px.colors.qualitative.Light24,
    "Set1": px.colors.qualitative.Set1,
    "Pastel1": px.colors.qualitative.Pastel1,
    "Dark2": px.colors.qualitative.Dark2,
    "Set2": px.colors.qualitative.Set2,
    "Pastel2": px.colors.qualitative.Pastel2,
    "Set3": px.colors.qualitative.Set3,
    "Antique": px.colors.qualitative.Antique,
    "Bold": px.colors.qualitative.Bold,
    "Pastel": px.colors.qualitative.Pastel,
    "Safe": px.colors.qualitative.Safe,
    "Vivid": px.colors.qualitative.Vivid,
    "Prism": px.colors.qualitative.Prism,
}


templates = [
    "bootstrap",
    "cerulean",
    "cosmo",
    "cyborg",
    "darkly",
    "flatly",
    "journal",
    "litera",
    "lumen",
    "lux",
    "materia",
    "minty",
    "morph",
    "pulse",
    "quartz",
    "sandstone",
    "simplex",
    "sketchy",
    "slate",
    "solar",
    "spacelab",
    "superhero",
    "united",
    "vapor",
    "yeti",
    "zephyr",
]

# Themes

themes_light_md = """
bootstrap  
![bootstrap](https://user-images.githubusercontent.com/72614349/197419065-925fbe32-0119-4c44-bc0a-6e663111abdc.png)  

cerulean  
![cerulean](https://user-images.githubusercontent.com/72614349/197419092-52732e45-dbc6-464a-a3aa-421460968e0a.png)  

cosmo  
![cosmo](https://user-images.githubusercontent.com/72614349/197419091-64c0e2e9-3c6b-4184-a856-d76c951b6b5e.png)  

flatly  
![flatly](https://user-images.githubusercontent.com/72614349/197419088-d17390bf-4958-4f09-aeb5-35363ef929a4.png)  

journal  
![journal](https://user-images.githubusercontent.com/72614349/197419087-0d82ef08-19e8-4157-8a95-2a5d6644ced2.png)  

literia  
![litera](https://user-images.githubusercontent.com/72614349/197419086-6824edf1-cb62-43c7-8da0-ccd994954af5.png)  

lumen  
![lumen](https://user-images.githubusercontent.com/72614349/197419085-24f459e5-44e7-4931-a96d-f45885721508.png)  

lux  
![lux](https://user-images.githubusercontent.com/72614349/197419084-d7afef46-2011-42fb-8ab2-5bdfe240b84c.png)  

materia  
![materia](https://user-images.githubusercontent.com/72614349/197419083-2b9185f8-a6df-4f21-b1a6-42fa764f636e.png)  

minty  
![minty](https://user-images.githubusercontent.com/72614349/197419082-187a231f-9b1f-4ee4-bf5d-d7247f8a1657.png)  


morph  
![morph](https://user-images.githubusercontent.com/72614349/197419079-c5682e3d-13e0-4fef-a72e-ece1f9f06256.png)

pulse  
![pulse](https://user-images.githubusercontent.com/72614349/197419078-a6c288a9-1aae-45a1-acdd-a70f1420a4d0.png)  


quartz  
![quartz](https://user-images.githubusercontent.com/72614349/197419077-49e5d8fd-da66-4811-9b7f-000ee82fa9c8.png)   

sandstone  
![sandstone](https://user-images.githubusercontent.com/72614349/197419075-2d016afc-24a0-4c7a-9a92-a3884824c650.png)  

simplex  
 ![simplex](https://user-images.githubusercontent.com/72614349/197419074-406c981b-1f75-4acd-b043-498dc24759c5.png)  
 
sketchy  
![sketchy](https://user-images.githubusercontent.com/72614349/197419073-bfc79243-54e8-4702-a467-225ea74105f5.png)  

superhero  
![superhero](https://user-images.githubusercontent.com/72614349/197419070-e5cb72f6-97a6-4c5f-b629-a33c0293bf38.png)  

united  
![united](https://user-images.githubusercontent.com/72614349/197419069-45b387c7-55d2-476c-9045-2bd09c6f80fa.png)  

yeti  
![yeti](https://user-images.githubusercontent.com/72614349/197419067-020a87ab-d273-44ec-b200-4b14cdc49d77.png)  

zephyr  
![zephyr](https://user-images.githubusercontent.com/72614349/197419066-3461f774-12bf-4884-8247-1626d4efc459.png)  

"""

theme_dark_md = """
cyborg  
![cyborg](https://user-images.githubusercontent.com/72614349/197419090-b7b49b9c-ab92-4311-8511-a82053bd91b8.png) 
 
darkly  
![darkly](https://user-images.githubusercontent.com/72614349/197419089-0dc4fc94-8ce2-4ae9-912c-5b3ac68756f5.png)  

slate  
![slate](https://user-images.githubusercontent.com/72614349/197419072-8c6011bc-41ee-4b65-a212-bc99a07c5b11.png)  

solar  
![solar](https://user-images.githubusercontent.com/72614349/197419071-46f03192-a2f4-4b7d-bbb0-1113ec9bef78.png)  

vapor   
![vapor](https://user-images.githubusercontent.com/72614349/197419068-1938734a-42e4-4b2a-858e-87240bc6c111.png)  

"""


themes_md = """
![bootstrap](https://user-images.githubusercontent.com/72614349/197419065-925fbe32-0119-4c44-bc0a-6e663111abdc.png)
![zephyr](https://user-images.githubusercontent.com/72614349/197419066-3461f774-12bf-4884-8247-1626d4efc459.png)
![yeti](https://user-images.githubusercontent.com/72614349/197419067-020a87ab-d273-44ec-b200-4b14cdc49d77.png)
![vapor](https://user-images.githubusercontent.com/72614349/197419068-1938734a-42e4-4b2a-858e-87240bc6c111.png)
![united](https://user-images.githubusercontent.com/72614349/197419069-45b387c7-55d2-476c-9045-2bd09c6f80fa.png)
![superhero](https://user-images.githubusercontent.com/72614349/197419070-e5cb72f6-97a6-4c5f-b629-a33c0293bf38.png)
![solar](https://user-images.githubusercontent.com/72614349/197419071-46f03192-a2f4-4b7d-bbb0-1113ec9bef78.png)
![slate](https://user-images.githubusercontent.com/72614349/197419072-8c6011bc-41ee-4b65-a212-bc99a07c5b11.png)
![sketchy](https://user-images.githubusercontent.com/72614349/197419073-bfc79243-54e8-4702-a467-225ea74105f5.png)
![simplex](https://user-images.githubusercontent.com/72614349/197419074-406c981b-1f75-4acd-b043-498dc24759c5.png)
![sandstone](https://user-images.githubusercontent.com/72614349/197419075-2d016afc-24a0-4c7a-9a92-a3884824c650.png)
![quartz](https://user-images.githubusercontent.com/72614349/197419077-49e5d8fd-da66-4811-9b7f-000ee82fa9c8.png)
![pulse](https://user-images.githubusercontent.com/72614349/197419078-a6c288a9-1aae-45a1-acdd-a70f1420a4d0.png)
![morph](https://user-images.githubusercontent.com/72614349/197419079-c5682e3d-13e0-4fef-a72e-ece1f9f06256.png)
![minty](https://user-images.githubusercontent.com/72614349/197419082-187a231f-9b1f-4ee4-bf5d-d7247f8a1657.png)
![materia](https://user-images.githubusercontent.com/72614349/197419083-2b9185f8-a6df-4f21-b1a6-42fa764f636e.png)
![lux](https://user-images.githubusercontent.com/72614349/197419084-d7afef46-2011-42fb-8ab2-5bdfe240b84c.png)
![lumen](https://user-images.githubusercontent.com/72614349/197419085-24f459e5-44e7-4931-a96d-f45885721508.png)
![litera](https://user-images.githubusercontent.com/72614349/197419086-6824edf1-cb62-43c7-8da0-ccd994954af5.png)
![journal](https://user-images.githubusercontent.com/72614349/197419087-0d82ef08-19e8-4157-8a95-2a5d6644ced2.png)
![flatly](https://user-images.githubusercontent.com/72614349/197419088-d17390bf-4958-4f09-aeb5-35363ef929a4.png)
![darkly](https://user-images.githubusercontent.com/72614349/197419089-0dc4fc94-8ce2-4ae9-912c-5b3ac68756f5.png)
![cyborg](https://user-images.githubusercontent.com/72614349/197419090-b7b49b9c-ab92-4311-8511-a82053bd91b8.png)
![cosmo](https://user-images.githubusercontent.com/72614349/197419091-64c0e2e9-3c6b-4184-a856-d76c951b6b5e.png)
![cerulean](https://user-images.githubusercontent.com/72614349/197419092-52732e45-dbc6-464a-a3aa-421460968e0a.png)

"""
