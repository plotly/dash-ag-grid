"""
Example Group Cell Renderer Configuration
https://www.ag-grid.com/react-data-grid/group-cell-renderer/

"""
import dash_ag_grid as dag
from dash import Dash, html


app = Dash(__name__)

data = {
    "Ireland": ["Dublin", "Galway", "Cork"],
    "UK": ["London", "Bristol", "Manchester", "Liverpool"],
    "USA": ["New York", "Boston", "L.A.", "San Fransisco", "Detroit"],
    "MiddleEarth": ["The Shire", "Rohan", "Rivendell", "Mordor"],
    "Midkemia": ["Darkmoor", "Crydee", "Elvandar", "LaMut", "Ylith"],
}

rowData = []
for country, cities in data.items():
    for city in cities:
        rowData.append(
            {
                "country": country,
                "type": "Non Fiction"
                if country in ["Ireland", "UK", "USA"]
                else "Fiction",
                "city": city,
            }
        )




columnDefs = [
    # this column shows just the country group values, but has not group renderer, so there is no expand / collapse functionality
    {
        "headerName": "Country Group - No Renderer",
        "showRowGroup": "country",
        "minWidth": 250,
    },
    # same as before, but we show all group values, again with no cell renderer
    {
        "headerName": "All Groups - No Renderer",
        "showRowGroup": True,
        "minWidth": 240,
    },
    # add in a cell renderer
    {
        "headerName": "Group Renderer A",
        "showRowGroup": True,
        "cellRenderer": "agGroupCellRenderer",
        "minWidth": 220,
    },
    # add in a field
    {
        "headerName": "Group Renderer B",
        "field": "city",
        "showRowGroup": True,
        "cellRenderer": "agGroupCellRenderer",
        "minWidth": 220,
    },
    # add in a cell renderer params
    {
        "headerName": "Group Renderer C",
        "field": "city",
        "minWidth": 240,
        "showRowGroup": True,
        "cellRenderer": "agGroupCellRenderer",
        "cellRendererParams": {
            "suppressCount": True,
            "checkbox": True,
            'innerRenderer': "SimpleCellRenderer",
            "suppressDoubleClickExpand": True,
            "suppressEnterExpand": True,
        },
    },
    {"headerName": "Type", "field": "type", "rowGroup": True},
    {"headerName": "Country", "field": "country", "rowGroup": True},
    {"headerName": "City", "field": "city"},
]

app.layout = html.Div(
    [
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=rowData,
            columnSize="autoSize",
            defaultColDef={"resizable": True},
            enableEnterpriseModules=True,
            dangerously_allow_code=True,
            dashGridOptions={
                "groupSelectsChildren": True,
                "groupDisplayType": "custom",
                "groupDefaultExpanded": 1,
                "rowSelection": "multiple",
            }
        ),
    ],
    style={"margin": 20},
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""

Add the following to the dashAgGridComponentFunctions.js file in the assets folder:
-------------------------

var dagcomponentfuncs = (window.dashAgGridComponentFunctions =
    window.dashAgGridComponentFunctions || {});


dagcomponentfuncs.SimpleCellRenderer = function (props) {
    return React.createElement(
        'span',
        {
            style: {
                backgroundColor: props.node.group ? 'coral' : 'lightgreen',
                padding: 2,
            },
        },
        props.value
    );
};

"""