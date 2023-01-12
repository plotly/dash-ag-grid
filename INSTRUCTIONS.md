Dash AG Grid is a Dash component wrapper for the AG Grid Javascript package, enabling you to display AG Grid tables natively in your Dash app.

The underlying AG Grid Javascript package is a third-party software component developed by AG Grid Ltd. Many AG Grid features are available for free in the AG Grid Community version. However, some features require a paid subscription to the AG Grid Enterprise version ([more info available here](https://www.ag-grid.com/license-pricing.php)). The demos in this app which use Enterprise features are clearly marked.

### Compatibility

The Dash AG Grid package requires Python version 3.6 or greater.

### Local installation instructions

1. Download the package directly from this app as a tarball: DOWNLOAD_LINK
2. Navigate to the folder where the package is contained and run:
    > ```bash
    > pip install dash_ag_grid-{0}.tar.gz
    > ```
3. Download one of the examples from this explorer by selecting a demo from the dropdown and run it locally once `dash_ag_grid` is installed.

### Deployment instructions

1. To deploy an app which uses the `dash_ag_grid` package to Dash Enterprise, include `dash_ag_grid-{0}.tar.gz` in the root of that app.
2. Add `dash_ag_grid-{0}.tar.gz` to your `requirements.txt` file.
3. Deploy the app as normal.
