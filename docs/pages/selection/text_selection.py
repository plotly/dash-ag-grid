from dash import  html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.utils import app_description
from utils.other_components import up_next, make_md, make_feature_card

register_page(
    __name__, order=8, description=app_description, title="Dash AG Grid - Text Selection"
)


text1 = """
# Cell Text Selection

If you are using AG Grid Enterprise, please see <dccLink href='/selection/range-selection' children='Range Selection' /> .  

In AG Grid Community, you can enable regular text selection as if the grid were a regular table.  Add the following to `dashGridOptions`:

```
dag.AgGrid(   
    dashGridOptions={"enableCellTextSelection": True, "ensureDomOrder": True},
    # other props...
) 
```
You can use this to select text and copy it to the browser's clipboard.  To see more on copying rows to the clipboard
 using the `dcc.Clipboard` component, see <dccLink href='/import-export/clipboard' children='Clipboard' /> page.
If you are using AG Grid Enterprise see [AG Grid Clipboard](https://www.ag-grid.com/react-data-grid/clipboard/)
 


"""

img= "https://user-images.githubusercontent.com/72614349/229208498-e1fee68b-5296-4c8b-903b-f905d261d082.png"


layout = html.Div(
    [
        make_md(text1),
        make_feature_card(img, ""),
        example_app("examples.import_export.clipboard_cell_text_selection", make_layout=make_tabs),


    ],
)
