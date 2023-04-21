from dash import Dash, html, dcc, register_page
import dash_bootstrap_components as dbc
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card

register_page(
    __name__, order=0, description=app_description, title="Dash AG Grid", path="/"
)

# #links
medium_article = "https://medium.com/plotly/announcing-dash-ag-grid-fbb4a1c83e62#:~:text=Dash%20AG%20Grid%20is%20a,grid%20accessible%20to%20our%20customers"
demo_app_img = "https://user-images.githubusercontent.com/72614349/215333840-5ab0acb4-6ac2-40b5-8eb8-2194ed11ba2d.png"
ag_grid_docs = "https://www.ag-grid.com/react-data-grid/"
ag_grid_docs_img = "https://user-images.githubusercontent.com/72614349/215338849-cb29d4e1-94b4-453a-84eb-5c8e05d3d742.png"
dash_ag_grid_github = "https://github.com/plotly/dash-ag-grid"



medium_article_card = dbc.Card(
    [
        dbc.CardImg(src=demo_app_img, top=True),
        dbc.CardBody(
            [
                html.Div("Medium", className="text-primary"),
                html.H4(
                    dcc.Link(
                        "Announcing Dash AG Grid", href=medium_article, target="_blank"
                    )
                ),
                html.Div(
                    "Written by: Plotly Community Manager, Adam Schroeder, and Plotly CTO and Co-Founder, Alex Johnson",
                    className="small",
                ),
            ]
        ),
    ],
    className="shadow my-2",
    style={"maxWidth": 400, "minHeight": 460},
)


ag_grid_docs_card = dbc.Card(
    [
        dbc.CardImg(src=ag_grid_docs_img, top=True),
        dbc.CardBody(
            [
                html.Div("Documentation", className="text-primary border-top pt-2"),
                html.H4(
                    dcc.Link(
                        "AG Grid Official Docs", href=ag_grid_docs, target="_blank"
                    )
                ),
                html.Div(
                    "See the official AG Grid docs for more info, including more features, demo apps and videos",
                    className="small",
                ),
            ]
        ),
    ],
    className="shadow my-2",
    style={"maxWidth": 400, "minHeight": 460},
)


text1 = """
# Dash AG Grid Documentation

Welcome to the Dash AG Grid documentation.  These docs are a Dash version of the [official AG Grid](https://www.ag-grid.com/react-data-grid/) documentation.  The structure, content and examples are similar to make it easier to use the upstream AG Grid  as a reference as well. 

"""

text2 = """  
>
> #### 🚧 This is a pre release version  
>  We have completed all planned breaking changes and doing the final review before the full 2.0.0 release!  
>
>  If you have tried previous alpha releases, see our <dccLink href-'/getting-started/migration-guide children='Migration Guide' />


### Getting Started

`pip install dash-ag-grid==2.0.0rc1`

 1. Read the [Medium article](https://medium.com/plotly/announcing-dash-ag-grid-fbb4a1c83e62#:~:text=Dash%20AG%20Grid%20is%20a,grid%20accessible%20to%20our%20customers) or watch the [webinar](https://www.youtube.com/watch?v=Ggekq7C5pz4?utm_source=Webinar%3A+AG+Grid+1%2F26%2F23&utm_medium=medium_article&utm_content=AnnouncingDashAGGrids) introducing Dash AG Grid.
 2. See the Plotly Video [Introducing Dash AG Grid](https://www.youtube.com/watch?v=dovf4FwtwPg)
 3. See the live [stock portfolio demo app](https://sales-demo.plotly.com/dash-ag-grid) from the webinar hosted by Plotly.
 4. Get the code for the demo app in [GitHub](https://github.com/plotly/dash-ag-grid/blob/dev/docs/demo_stock_portfolio.py)
 5. Learn more about [AG Grid](https://www.ag-grid.com/react-data-grid) in the upstream docs, including more information on community features and licensing for the enterprise version.
 
Note that the webinar and Medium article are based on the first alpha release 2.0.0a1.  Please be sure to see the updated
 code for the [demo_stock_portfolio.py](https://github.com/plotly/dash-ag-grid/blob/dev/docs/demo_stock_portfolio.py)) app.
 
### Contributing

Feedback is welcome!  Please feel free to open an [issue]( https://github.com/plotly/dash-ag-grid/issues) on GitHub.

dash-ag-grid component
 - Community pull requests are welcome.  Find information on how to build and run a local development version of dash-ag-grid on [GitHub](https://github.com/plotly/dash-ag-grid)

Dash Ag Grid documentation
 - These docs are under development as well.  There are many examples in the official AG Grid docs that have not been
included here yet.  Please open an issue or do pull requests for edits or to add examples. Or post your
question, comments or demo apps on the Dash Community Forum.
 


### Feature Preview

Below you will find just a few examples to get you started.  

👈 See more examples in each section of the docs.
"""

text_callbacks = """
### AG Grid with Dash callbacks

This is the sample app from the [webinar](https://www.youtube.com/watch?v=Ggekq7C5pz4?utm_source=Webinar%3A+AG+Grid+1%2F26%2F23&utm_medium=medium_article&utm_content=AnnouncingDashAGGrid).  See the app [live]((https://sales-demo.plotly.com/dash-ag-grid)), get the [code](https://github.com/plotly/dash-ag-grid/blob/dev/docs/demo_stock_portfolio.py) in GitHub

This grid uses the `selectedRows` prop to update the stock price figure, and the `cellValueChanged` prop in to update the
 pie chart in callbacks. 
"""
img_callbacks = "https://user-images.githubusercontent.com/72614349/215555251-6e4a3248-d789-449d-8036-7e84a43c1b63.gif"

text_columns = """
### Columns

In the Columns section, learn how to:
  - Set up the [column definitions](/columns/column-definitions), group columns, align content right and left and more. 
  - [Update](/columns/updating-definitions) the column defs in a callback, including adding and removing columns.
  - Format the [headers](/columns/column-headers) including setting the heights, text orientation, and header tooltips.
  - Make multi-level [Column Groups](/columns/column-groups)
  - Enable sizing, moving and pinning columns (see example below)
"""
img_columns = "https://user-images.githubusercontent.com/72614349/215576691-789036d0-30bc-48fb-a056-a393ef4e4e82.gif"


text_rows = """
### Rows

In the Rows section learn how to: 
 - Get default [row ids](/rows/row-ids), or assign row id's based on the data in the grid.
 - [Sort](/rows/row-sorting) the data by clicking on the header.
 - Allow user to rearrange the rows by [dragging](/rows/row-ragging) with a mouse 
"""
img_rows = "https://user-images.githubusercontent.com/72614349/215598823-4c810d64-43ce-431d-ae66-57d860a7f594.gif"


text_style = """
### Layout & Style

In this sections, learn how to select a [theme](/layout/selections), style rows and cells, customize colors, fonts,borders, headers and selections.

In the example below, this dark theme is set with `className="ag-theme-alpine-dark"`.  We use conditional formatting to
set the background color of the "Shares" column.  We also set the cell background color based on the content --red for "sell" and green for "buy".
 """
img_style = "https://user-images.githubusercontent.com/72614349/215599866-3e9ead07-40a6-4a90-8bf0-538c288cd18c.gif"


text_selection = """
### Selection
In this section, learn how to set single or multi select.  In the stock portfolio app above it is set to select a
 single row on click with `rowSelection='single'`.  In the example below, it's set to multi-select with check boxes.
 You can also select or deselect all with the button in the header.
 

"""
img_selection = "https://user-images.githubusercontent.com/72614349/215606692-f4be4fb8-8911-4647-9a50-692e7bca989f.gif"


text_animation = """
### Rendering - Animation

In the [Rendering](/rendering/animation-renderer) section learn how to add cell change animations. You can see it in action when you change
 the share quantity in the stock portfolio demo app, and in the example below.

"""
img_animation = "https://user-images.githubusercontent.com/72614349/215603780-39c838d2-e757-43ac-84c3-6d0b47fb9028.gif"


text_editing = """
### Editing

In the [Editing](/editing/overview) section learn how to:
 - Enable editing,
 - Various ways to [start and stop editing](/editing/start-stop-editing) such as hitting enter, tab, single click edit, and more.
 - Make the [Cell Editors](/editing/cell-editors) in-line or popup above or below the cell
 - Use [Provided Cell Editors](/editing/provided-cell-editors) such a(s the text input, html.Select, large text area editor.
 - Enable the [Undo Redo](/editing/undo-redo) using ctrl-z and ctrl-y
 - Enable [Full Row](/editing/full-row) editing to make all cells in the row become editable at the same time.
 
 Below is an example of the provided cell editors:
"""
img_editing = "https://user-images.githubusercontent.com/72614349/215611299-f3963c99-762f-4e0c-b119-9318d21d8401.gif"


text_components_markdown = """
### Components - Markdown

In the [Components](/components/markdown) section learn how to use the two custom components included with dash-ag-grid:
- [Markdown] - use this like the dcc.Markdown component
- [Row Menu] - use this to allow for custom options for a row, column or cell.  The selections are available in a callback
"""
img_components_markdown = "https://user-images.githubusercontent.com/72614349/215612660-c85bdb7b-7b90-4836-a5c5-6ca0678db395.png"


text_components_rowmenu = """
### Components - Row Menu

In the [Components](/components/markdown) section learn how to use the two custom components included with dash-ag-grid:
- [Markdown] - use this like the dcc.Markdown component
- [Row Menu] - use this to allow for custom options for a row, column or cell.  The selections are available in a callback
"""
img_components_rowmenu = "https://user-images.githubusercontent.com/72614349/215612845-32a812bf-f6ba-404e-befc-a59af137d3f7.gif"

text_enterprise = """
### Enterprise Features
See the [Enterprise](/enterprise) section and the AG Grid documentation for more information about AG Grid enterprise features and
 licensing.
"""

layout = html.Div(
    [
        make_md(text1),
        dbc.Row(
            [
                dbc.Col(medium_article_card, md=6),
                dbc.Col(ag_grid_docs_card, md=6),
            ],
            className="px-5",
        ),
        make_md(text2),
        make_feature_card(img_callbacks, text_callbacks),
        make_feature_card(img_columns, text_columns),
        make_feature_card(img_rows, text_rows),
        make_feature_card(img_style, text_style),
        make_feature_card(img_selection, text_selection),
        make_feature_card(img_animation, text_animation),
        make_feature_card(img_editing, text_editing),
        make_feature_card(img_components_markdown, text_components_markdown),
        make_feature_card(img_components_rowmenu, text_components_rowmenu),
        make_md(text_enterprise),
    ],
)
