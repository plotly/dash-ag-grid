from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Layout and Style - Themes",
)

text1 = """
# Themes

The grid is styled with CSS, and a theme is simply a CSS class that applies styles to the grid. Most users choose a provided theme and then customise it to meet their needs. It is also possible to create your own themes.

### Provided Themes
The grid comes with several provided themes which act as a great starting point for any application-specific customisations.

__Alpine__
- ag-theme-alpine
- ag-theme-alpine-dark  
 

Modern looking themes with high contrast, and generous padding.  

__Recommendation__: This is the recommended grid theme and an excellent choice for most applications.  It is the default theme for Dash apps.

------------------
__Balham__
- ag-theme-balham
- ag-theme-balham-dark  

Themes for professional data-heavy applications     

__Recommendation__: Balham was the recommended theme before Alpine was developed. It is still an excellent choice for applications that need to fit more data onto each page.

------------------

__Material__
- ag-theme-material  

A theme designed according to the Google Material Language Specs.  

__Recommendation__: This theme looks great for simple applications with lots of white space, and is the obvious choice if the rest of your application follows the Google Material Design spec. However, the Material spec doesn't cater for advanced grid features such as grouped columns and tool panels. If your application uses these features, consider using ag-theme-alpine instead.

-----------------

__Bootstrap__
- ag-bootstrap  

A theme designed to work well with Bootstrap theme.

` `  

` `  

` `  

### Applying a Theme to an App

All the themes are loaded for you by the dash-ag-grid component.  To use a theme, add the theme to the `className` 
prop in the component or a html.Div or other element that contains your grid. The following is an example of using the Alpine dark theme:

```
    dag.AgGrid(
        className="ag-theme-alpine-dark",
        # other props    
    )
```

Note that in Dash, the default is `className="ag-theme-alpine"`, so it's not necessary to set this every time.  For example:

```
    dag.AgGrid(
        # No need to set the className since this is the default:
        # className="ag-theme-alpine",
        # other props 
    )
```


However, if you add other class names, it's necessary to include the theme, even when you use the default theme.  
And remember to include the theme if you update the `className` prop in a callback too!  

````
dag.AgGrid(
        # always include the theme when adding other classes:
        className="ag-theme-alpine m-4",
        # other props 
    )
````

> The grid must always have a theme class set on its container, whether this is a provided theme or your own.  The default is `className="ag-theme-alpine"`

### Loading CSS files
For the CSS to work as expected, the stylesheets need to be added in the correct order.  However, Dash loads
 the stylesheets in a certain way.  Here's the order:
 
 1. Files included as external stylesheets in the app constructor `app=Dash(__name__, external_stylesheets=[])` 
  
 2. `.css` files in the `/assets` folder, in alphanumerical order by filename
 
 3. The grid's stylesheets when you `import dash_ag_grid`
 
It's important to keep this in mind when modifying or creating your own themes for dash-ag-grid.  For more information,
 on adding `.css` and `.js` files with Dash, see the [Dash docs](https://dash.plotly.com/external-resources).
 
` `  

` `  
` `  


### Customizing the theme

You can modify the theme by making global changes or creating a class and combining it with the theme.

#### Global changes

To change the theme globally, you can make changes to the theme like the snippet below.  
Note that it's necessary to use `!important` because the `.css` files in the `/assets` folder are loaded before the grid's theme.


```css
/* set the background color of many elements across the grid */
.ag-theme-alpine {
    --ag-background-color: #ddd !important;
}
/* change the font style of a single UI component */
.ag-theme-alpine .ag-header-cell-label {
    font-style: italic !important;
}
```


### Creating a class to use with a theme

To create a reusable set of design customisations that can be shared between projects you can use a CSS class that is
 applied in addition to the theme you're modifying. 

The grid wrapper element should specify both the class name of the theme you're modifying, and the name of the 
custom theme. Since with Dash, your custom theme is loaded before the base theme, it's necessary to difine it the following
way in the `.css` file in the `/assets` folder:

```css
.ag-theme-alpine.ag-theme-acmecorp {
    --ag-odd-row-background-color: #aaa;
}
```
Then to use it in the app:

```python
    dag.AgGrid(
        className="ag-theme-alpine ag-theme-acmecorp",
        # other props
    )
```


### Creating your own theme (from scratch)
The majority of users select a provided theme and make customisations using CSS. If your chosen provided theme has
 elements that you don't want, you will need to add CSS rules to remove them. If your desired look and feel is very
  different from the provided theme, at some point it becomes easier to start from scratch. To do this, you can define your own theme.

A theme is simply a CSS class name matching the pattern `ag-theme-*`, along with CSS rules that target this class name.

Ensure that grid `.css` is file is located in the `/assets` folder and/or is loaded as an `external_stylesheet`.  Choose a theme name and apply it to the grid:

```
className="ag-theme-custom-theme"
```

That's it! You've created a theme. You haven't added any styles to it so what you will see is a nearly blank slate - basic customisable borders and padding but no opinionated design elements. You can then add customisations using CSS:

```
.ag-theme-custom-theme {
    /* customise with CSS variables */
    --ag-grid-size: 8px;
    --ag-border-color: red;
}
.ag-theme-custom-theme .ag-header {
    /* or with CSS selectors targeting grid DOM elements */
    font-style: italic;
}
```
### CSS Variable Reference

 - [CSS variables](https://www.ag-grid.com/react-data-grid/global-style-customisation-variables/) in the AG Grid docs.

 - [All available icons](https://www.ag-grid.com/react-data-grid/custom-icons/#provided-icons) for each provided theme in the AG Grid docs.

 - Tips on using custom CSS with the grid in the [Advanced CSS](https://www.ag-grid.com/react-data-grid/global-style-customisation-css/) section of the AG Grid docs.

 - Details of the CSS Variables, go to the link as described below:
 
    ```
    https://cdn.jsdelivr.net/npm/ag-grid-community@< ag grid version>/styles/ag-grid.css" 
    ```
    
    For example, if you are using dash-ag-grid==2.0.0, it uses ag-grid 29.3.3
    ```
    https://cdn.jsdelivr.net/npm/ag-grid-community@29.3.3/styles/ag-grid.css
    ```

` `  
` `

` `
### Examples of Themes
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.themes", make_layout=make_tabs),
        # up_next("text"),
    ],
)
