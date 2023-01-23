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
            # if file in names:
            #     raise Exception(
            #         f"filenames must be unique.  `{file}.py` already exists"
            #     )
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
