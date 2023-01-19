"""
provided cell editors - text, select, textarea
"""

import dash_ag_grid as dag
from dash import Dash, html, dcc

app = Dash(__name__)


columnDefs = [
    {
        "headerName": "Text Editor",
        "field": "task",
        "cellEditor": "agTextCellEditor",
        "cellEditorParams": {
            "maxLength": 20,
        },
    },
    {
        "headerName": "Select Editor",
        "field": "color",
        "cellEditor": "agSelectCellEditor",
        "cellEditorParams": {
            "values": ["red", "yellow", "green"],
        },
    },
    {
        "headerName": "Large Text Editor",
        "field": "description",
        "cellEditorPopup": True,
        "cellEditor": "agLargeTextCellEditor",
        "cellEditorParams": {
            "maxLength": 250,
            "rows": 10,
            "cols": 50,
        },
        "flex": 2,
    },
]


descriptiion = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
rowData = [
    {"task": "task 1", "color": "green", "description": descriptiion},
    {"task": "task 2", "color": "yellow", "description": descriptiion},
    {"task": "task 3", "color": "red", "description": descriptiion},
]


app.layout = html.Div(
    [
        dcc.Markdown(
            "This grid has a regular text editor, select dropdown, and a large textarea editor."
        ),
        dag.AgGrid(
            id="cell-editor-grid",
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="sizeToFit",
            defaultColDef={"editable": True, "sortable": True},
        ),
        html.Div(id="cell-editor-div"),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=False)
