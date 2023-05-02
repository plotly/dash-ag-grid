# Dash AG Grid

Dash AG Grid is a Dash component wrapper for the AG Grid JavaScript package, enabling you to display AG Grid components natively in your Dash app.

The underlying AG Grid JavaScript package is a third-party software component developed by [AG Grid Ltd](http://www.ag-grid.com/). Many features are available for free in the AG Grid [Community version](https://github.com/ag-grid/ag-grid). Some features require a paid subscription to the AG Grid Enterprise version ([more info available here](https://www.ag-grid.com/license-pricing.php)). Both the community and enterprise versions are included in this component, but the enterprise features require you to provide a valid AG Grid license key. The demos which use Enterprise features are clearly marked.


## v2.0.0 Release

If you have tried v2.0.0 alpha releases, release candidates, or our v1.x enterprise package, please see our [Migration Guide](https://dash.plotly.com/dash-ag-grid/migration-guide) (previously hosted [here](https://dashaggrid.pythonanywhere.com/getting-started/migration-guide)).


### Getting Started

`pip install dash-ag-grid`

1. Read the [Medium article](https://medium.com/plotly/announcing-dash-ag-grid-fbb4a1c83e62#:~:text=Dash%20AG%20Grid%20is%20a,grid%20accessible%20to%20our%20customers) or watch the [webinar](https://www.youtube.com/watch?v=Ggekq7C5pz4?utm_source=Webinar%3A+AG+Grid+1%2F26%2F23&utm_medium=medium_article&utm_content=AnnouncingDashAGGrids) introducing Dash AG Grid.
2. See the live [stock portfolio demo app](https://sales-demo.plotly.com/dash-ag-grid) from the webinar hosted by Plotly.
3. Get the code for the demo app in [GitHub](https://github.com/plotly/dash-ag-grid/blob/dev/docs/demo_stock_portfolio.py)
4. Learn more about [AG Grid](https://www.ag-grid.com/react-data-grid) in the upstream docs, including more information on community features and licensing for the enterprise version.


### Documentation
At v2.0.0 release we're still working to move all the Dash AG Grid docs into the official Dash docs, https://dash.plotly.com/dash-ag-grid.
In the meantime you can find them all here: https://dashaggrid.pythonanywhere.com/

![docs_app](https://user-images.githubusercontent.com/72614349/233876110-4a29348c-d8e3-4114-b152-bf97f934eac8.png)


## Contributing

Dash AG Grid welcomes community contributions!

If you have identified a bug or have an idea for a new feature, it's best to start with a GitHub issue. First look at existing issues at https://github.com/plotly/dash-ag-grid/issues to make sure this is not a duplicate. Then create a new issue. Bug reports should be accompanied by a small example app that someone else can copy and run to reproduce the problem.

The docs are under development as well. There are many examples in the official AG Grid docs that have not been included here yet. Please open an issue or do pull requests for edits or to add examples. Or post your question, comments or demo apps on the [Dash Community Forum](https://community.plotly.com/).

### Running the docs app locally
```
cd docs/
pip install -r requirements.txt
```
Then you can run the apps there:
- `demo_stock_portfolio.py` and `demo_stock_portfolio_simple.py` are small apps demonstrating some key features of Dash AG Grid, such as calculated columns, conditional formatting, and connecting its data and selected rows to graphs.
- `app.py` runs a comprehensive documentation app. After we complete the open-source release, this will be merged into the main dash docs at https://dash.plotly.com/ but right now this app is the best way to explore Dash AG Grid.

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
