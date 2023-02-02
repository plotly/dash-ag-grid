from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Layout and Style",
)


text1 = """
# Customising Colors & Fonts

Change the overall color scheme and appearance of data.

The grid exposes many CSS `--ag-*-color` variables that affect the colour of elements. `--ag-font-size` and `--ag-font-family` control the default font for the grid.

Example
```
.ag-theme-alpine {
    --ag-foreground-color: rgb(126, 46, 132);
    --ag-background-color: rgb(249, 245, 227);
    --ag-header-foreground-color: rgb(204, 245, 172);
    --ag-header-background-color: rgb(209, 64, 129);
    --ag-odd-row-background-color: rgb(0, 0, 0, 0.03);
    --ag-header-column-resize-handle-color: rgb(126, 46, 132);

    --ag-font-size: 17px;
    --ag-font-family: monospace;
}
```
The above code would apply to every grid with the ag-theme-alpine.  In this example we also add a .color-font class so
it will only apply to this example. 

"""


text2 = """

### Key colour variables
Some of the most important colour variables are listed below. For the full list check the full CSS variables reference - every colour variable is ends with -color.

 - `--ag-alpine-active-color` CSS color (e.g. `red` or `#fff`) (Alpine theme only) accent colour used for checked checkboxes, range selections, row hover, row selections, selected tab underlines, and input focus outlines in the Alpine theme
 - `--ag-balham-active-color` CSS color (e.g. `red` or `#fff`)(Balham theme only) accent colour used for checked checkboxes, range selections, row selections, and input focus outlines in the Balham theme
 - `--ag-material-primary-color` CSS color (e.g. `red` or `#fff`) (Material theme only) the primary colour as defined in the Material Design colour system. Currently this is used on buttons, range selections and selected tab underlines in the Material theme
 - `--ag-material-accent-color` CSS color (e.g. `red` or `#fff`) (Material theme only) the accent colour as defined in the Material Design colour system. Currently this is used on checked checkboxes in the Material theme
 - `--ag-foreground-color` CSS color` (e.g. `red` or `#fff`) Colour of text and icons in primary UI elements like menus
 - `--ag-background-color CSS color` (e.g. `red` or `#fff`) Background colour of the grid
 - `--ag-secondary-foreground-color` CSS color (e.g. `red` or `#fff`) Colour of text and icons in UI elements that need to be slightly less emphasised to avoid distracting attention from data
 - `--ag-data-color CSS color` (e.g. `red` or `#fff`) Colour of text in grid cells
 - `--ag-header-foreground-color` CSS color (e.g. `red` or `#fff`) Colour of text and icons in the header
 - `--ag-header-background-color` CSS color (e.g. `red` or `#fff`) Background colour for all headers, including the grid header, panels etc
 - `--ag-disabled-foreground-color` CSS color (e.g. `red` or `#fff`) Color of elements that can't be interacted with because they are in a disabled state
 - `--ag-odd-row-background-color` CSS color (e.g. `red` or `#fff`) Background colour applied to every other row
 - `--ag-row-hover-color` CSS color (e.g. `red` or `#fff`) Background color when hovering over rows in the grid and in dropdown menus. Set to transparent to disable the hover effect. Note: if you want a rollover on one but not the other, use CSS selectors instead of this property
 - `--ag-border-color`  CSS color (e.g. `red` or `#fff`) Colour for border around major UI components like the grid itself, headers; footers and tool panels.
 - `--ag-row-border-color` CSS color (e.g. `red` or `#fff`) Colour of the border between grid rows, or transparent to display no border

>
> There are a lot of colour variables - the easiest way to find the variable that colours a specific element is often to inspect the element in your browser's developer tools and check the value of its color or background-color properties.
>


### Colour blending, Sass and CSS
The Sass API Colour Blending feature will automatically generate a few default values for colour variables based on the ones that you define. If you're using CSS you may want to set these values yourself for a consistent colour scheme:

Setting --ag-alpine-active-color in the Sass API will:

 - Set --ag-selected-row-background-color to a 10% opaque version
- Set --ag-range-selection-background-color to a 20% opaque version
- Set --ag-row-hover-color to a 10% opaque version
- Set --ag-column-hover-color to a 10% opaque version
- Set --ag-input-focus-border-color to a 40% opaque version
- Setting --ag-balham-active-color in the Sass API will:

- Set --ag-selected-row-background-color to a 10% opaque version
- Set --ag-range-selection-background-color to a 20% opaque version


> ### Generating semi-transparent colours
>
> To make a semi-transparent version of a colour, you can use one of these techniques. If your colour is defined as a 6-digit hex value (#RRGGBB) convert it to an 8-digit hex value (#RRGGBBAA). If your colour is defined as a rgb value (rgb(R, G, B)) add a fourth value to specify opacity (rgb(R, G, B, A)).
>
>So for example, the color deeppink is hex #FF1493 or rgb rgb(255, 20, 147).

> - 10% opaque: #8800EE1A or rgb(255, 20, 147, 0.1)
> - 20% opaque: #8800EE33 or rgb(255, 20, 147, 0.2)
> - 30% opaque: #8800EE4D or rgb(255, 20, 147, 0.3)
> - 40% opaque: #8800EE66 or rgb(255, 20, 147, 0.4)
> - 50% opaque: #8800EE80 or rgb(255, 20, 147, 0.5)
"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.layout.color_font", make_layout=make_tabs),
        make_md(text2),
        # up_next("text"),
    ],
)
