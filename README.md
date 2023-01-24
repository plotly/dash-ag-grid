# Dash AG Grid

Dash AG Grid is a Dash component wrapper for the AG Grid Javascript package, enabling you to display AG Grid tables natively in your Dash app.

The underlying AG Grid Javascript package is a third-party software component developed by [AG Grid Ltd](http://www.ag-grid.com/). Many AG Grid features are available for free in the AG Grid [Community version](https://github.com/ag-grid/ag-grid). However, some features require a paid subscription to the AG Grid Enterprise version ([more info available here](https://www.ag-grid.com/license-pricing.php)). The demos which use Enterprise features are clearly marked.

**Dash AG Grid is currently a prerelease**

We're working hard to get it ready for its initial v2.0.0 open-source release on PyPI. In the meantime if you'd like to try it out, you can clone this repo and follow the instructions in _Developing in this repo_ below to build the component and install it in development mode. At that point you can use `import dash_ag_grid as dag` in your own app. There are two apps in the `docs/` folder that you can run to learn about the component. To run these, first install the docs requirements:
```
cd docs/
pip install -r requirements.txt
```
Then you can run the apps there:
- `demo_stock_portfolio.py` and `demo_stock_portfolio_simple.py` are small apps demonstrating some key features of Dash AG Grid, such as calculated columns, conditional formatting, and connecting its data and selected rows to graphs.
- `app.py` runs a comprehensive documentation app. After we complete the open-source release, this will be merged into the main dash docs at https://dash.plotly.com/ but right now this app is the best way to explore Dash AG Grid.

## Contributing

Dash AG Grid welcomes community contributions!

If you have identified a bug or have an idea for a new feature, it's best to start with a GitHub issue. First look at existing issues at https://github.com/plotly/dash-ag-grid/issues to make sure this is not a duplicate issue. Then create a new issue. Bug reports should be accompanied by a small example app that someone else can copy and run to reproduce the problem.

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

Create source and wheel distributions in the generated `dist/` folder, after emptying out any previous builds:
```
rm -rf dist
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
