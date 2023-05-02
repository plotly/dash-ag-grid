import json
from setuptools import setup


with open("package.json") as f:
    package = json.load(f)

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author=package["author"],
    packages=[package_name],
    include_package_data=True,
    license=package["license"],
    description=package.get("description", package_name),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["dash>=2"],
    python_requires=">=3.6",
    url="https://dash.plotly.com/dash-ag-grid",
    project_urls={
        "Documentation": "https://dash.plotly.com/dash-ag-grid",
        "Source": "https://github.com/plotly/dash-ag-grid",
        "Issue Tracker": "https://github.com/plotly/dash-ag-grid/issues",
    },
    classifiers = [
        "Framework :: Dash",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
