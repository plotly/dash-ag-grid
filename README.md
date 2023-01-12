# dash-ag-grid

dash-ag-grid is a Dash component library.

## Install dependencies

If you have selected install_dependencies during the prompt, you can skip this part.

1. Install npm packages
    ```
    $ npm install
    ```
2. Create a virtual env and activate.

    ```
    $ virtualenv venv
    $ . venv/bin/activate
    ```

    _Note: venv\Scripts\activate for windows_

3. Install python packages required to build components.
    ```
    $ pip install -r requirements.txt
    ```
4. Install the python packages for testing (optional)
    ```
    $ pip install -r tests/requirements.txt
    ```

### Create a production build:

1. Build the code:
    ```
    $ npm run build
    ```
2. Run the docs locally:
    ```
    $ python usage.py
    ```
3. Create a Python distribution
    ```
    $ python setup.py sdist bdist_wheel
    ```
    This will create source and wheel distribution in the generated the `dist/` folder.
    See [PyPA](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project)
    for more information.
