import dash_ag_grid as dag
from dash import Dash, html, dcc
import pandas as pd

app = Dash(__name__)


df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/ag-grid/olympic-winners.csv"
)

columnDefs = [
    # Row group by country and by year is enabled.
    {
        "field": "country",
        "rowGroup": True,
        "hide": True,
        "suppressColumnsToolPanel": True,
    },
    {
        "field": "sport",
        "rowGroup": True,
        "hide": True,
        "suppressColumnsToolPanel": True,
    },
    {
        "field": "year",
        "pivot": True,
        "hide": True,
        "suppressColumnsToolPanel": True,
    },
    {
        "field": "gold",
        "sortable": True,
        "filter": True,
        "aggFunc": "sum",
        "cellStyle": {
            "styleConditions": [
                {"condition": "params.value > 100", "style": {"color": "red"}}
            ]
        },
    },
    {"field": "silver", "sortable": True, "filter": True, "aggFunc": "sum"},
]

app.layout = html.Div(
    [
        dcc.Markdown(
            """
            Demonstration of row groupings in a Dash AG Grid.
            This grid groups first by country and then by year.
            Note that the row background color is set only on the row groupings (gold<3) and not on the row detail level.
            """
        ),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=dict(
                resizable=True,
                rowSelection="multiple",
                suppressAggFuncInHeader=True,
            ),
            enableEnterpriseModules=True,
            getRowStyle={
                "styleConditions": [
                    {
                        "condition": "params.node.aggData ? params.node.aggData.gold < 3 : false",
                        "style": {"backgroundColor": "silver"},
                    }
                ]
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
debugging tip - using  `log(params)` 

The following will print to the browser console all the params available when using `getRowStyle`

getRowStyle={'styleConditions':[{'condition': 'log(params)', 'style': {}}]}

For more info see: 
   https://dashaggrid.pythonanywhere.com/getting-started/beyond-the-basics
   https://community.plotly.com/t/ag-grid-row-wise-styling/72345/23


"""
