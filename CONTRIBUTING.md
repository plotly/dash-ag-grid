
# Dash AG Grid Contributing Guide

Dash AG Grid welcomes community contributions!

If you have identified a bug or have an idea for a new feature, it's best to start with a GitHub issue. First look at existing issues at https://github.com/plotly/dash-ag-grid/issues to make sure this is not a duplicate. Then create a new issue. Bug reports should be accompanied by a small example app that someone else can copy and run to reproduce the problem.

If you have questions, please ask on the [Dash Community Forum](https://community.plotly.com/). rather than using GitHub issues.


### Developing in this repo

Make sure you have Dash installed with dev and testing extras:
```
pip install dash[dev,testing]
```
Build the component (from the root of this repo):
```
npm i
npm run build
```
Now install the component in development mode:
```
$ pip install -e .
```
In development mode, Python uses the files in this directory when you import the package. So you can write a testing app in another folder, and whenever you change some code and rebuild the component here it will update in your testing app.

### Create a production build

Update the package version is correct in `package.json` and `CHANGELOG.md` and the changelog lists all the important updates. Then reinstall (so `package-lock.json` gets the new version) and rebuild:
```
npm i
npm run build
```

Create source and wheel distributions in the generated `dist/` folder, after emptying out any previous builds:
```
rm -rf dist build
python setup.py sdist bdist_wheel
```
See [PyPA](https://packaging.python.org/guides/distributing-packages-using-setuptools/#packaging-your-project)
for more information.
Then use [`twine`](https://pypi.org/project/twine/) to upload these to PyPI:
```
twine upload dist/*
```
We also publish the JavaScript build to NPM, so `unpkg` has the bundles if users set `serve_locally=False`. First make a test of the NPM package, verify that its contents are reasonable:
```
npm pack
```
Then publish:
```
npm publish
```
