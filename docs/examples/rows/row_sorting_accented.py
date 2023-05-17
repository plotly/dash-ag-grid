"""
Example Accented Sort taking into account locale-specific characters
"""

import dash
import dash_ag_grid as dag
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

data = [
    {'accented': 'aäàá'},
    {'accented': 'aáàä'},
    {'accented': 'aàáä'},
]

columnDefs = [
    {"headerName": "Row ID", "valueGetter": {"function": "params.node.id"}, 'width': 100},
    {'field': 'accented', 'width': 150}
]

defaultColDef = {"sortable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Example: Accented Sort"),
        dbc.Switch(id="switch-accented-sorting", label="Enable accented sorting"),
        dag.AgGrid(
            id="grid-row-accented-sorting",
            columnDefs=columnDefs,
            rowData=data,
            defaultColDef=defaultColDef,
        ),
    ]
)


@app.callback(
    Output("grid-row-accented-sorting", "dashGridOptions"),
    Input("switch-accented-sorting", "value"),
)
def enable_accented_sort(switch_checked):
    return {
        'animateRows': True,
        'accentedSort': switch_checked  # True if switch ON, False if switch OFF
    }


if __name__ == "__main__":
    app.run_server(debug=True)
