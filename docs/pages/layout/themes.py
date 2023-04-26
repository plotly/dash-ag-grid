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

File name `ag-theme-alpine[.min].css`	 

Modern looking themes with high contrast, and generous padding.  

__Recommendation__: This is the recommended grid theme and an excellent choice for most applications.  It is the default theme for Dash apps.

------------------
__Balham__
- ag-theme-balham
- ag-theme-balham-dark  

File name `ag-theme-balham[.min].css`	
Themes for professional data-heavy applications     

__Recommendation__: Balham was the recommended theme before Alpine was developed. It is still an excellent choice for applications that need to fit more data onto each page.

------------------

__Material__
- ag-theme-material  

File name `ag-theme-material[.min].css`	
A theme designed according to the Google Material Language Specs.  

__Recommendation__: This theme looks great for simple applications with lots of white space, and is the obvious choice if the rest of your application follows the Google Material Design spec. However, the Material spec doesn't cater for advanced grid features such as grouped columns and tool panels. If your application uses these features, consider using ag-theme-alpine instead.

-----------------

__Bootstrap__
- ag-bootstrap  

File name `ag-theme-bootstrap[.min].css` 

A theme designed to work well with Bootstrap theme.

` `  

` `  

` `  


### Applying a Theme to an App
To use a theme, add the theme to the `className` prop in the component or a html.Div or other element that contains your grid. The following is an example of using the Alpine theme:

> The grid must always have a theme class set on its container, whether this is a provided theme or your own.  The default is `className="ag-theme-alpine"`

### Creating your own theme
The majority of users select a provided theme and make customisations using CSS. If your chosen provided theme has elements that you don't want, you will need to add CSS rules to remove them. If your desired look and feel is very different from the provided theme, at some point it becomes easier to start from scratch. To do this, you can define your own theme.

A theme is simply a CSS class name matching the pattern `ag-theme-*`, along with CSS rules that target this class name.

Ensure that ag-grid.css is located in the `/assets` folder and/or is loaded as an `external_stylesheet`.  Choose a theme name and apply it to the grid:

```
className="ag-theme-mycustomtheme"
```

That's it! You've created a theme. You haven't added any styles to it so what you will see is a nearly blank slate - basic customisable borders and padding but no opinionated design elements. You can then add customisations using CSS:

```
.ag-theme-mycustomtheme {
    /* customise with CSS variables */
    --ag-grid-size: 8px;
    --ag-border-color: red;
}
.ag-theme-mycustomtheme .ag-header {
    /* or with CSS selectors targeting grid DOM elements */
    font-style: italic;
}
```
### CSS Variable Reference

See all the [CSS variables](https://www.ag-grid.com/react-data-grid/global-style-customisation-variables/) in the AG Grid docs.

See a list with [all available icons](https://www.ag-grid.com/react-data-grid/custom-icons/#provided-icons) fore each provided theme in the AG Grid docs


"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.themes", make_layout=make_tabs),
        # up_next("text"),
    ],
)
