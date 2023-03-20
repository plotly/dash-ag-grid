from dash import Dash, html, dcc
import dash_ag_grid as dag
import plotly.express as px

df = px.data.stocks()

app = Dash(__name__)

columnDefs = [
    {
        "field": "date",
        "filter": "agDateColumnFilter",
        "valueGetter": {"function": "d3.timeParse('%Y-%m-%d')(params.data.date)"},
        "valueFormatter": {"function": "d3.timeFormat('%m/%d/%Y')(params.value)"},
        "floatingFilter": True,
    }
] + [{"field": i} for i in df.columns if i != "date"]

defaultColDef = {"sortable": True}

app.layout = html.Div(
    [
        dcc.Markdown("Date formatting example."),
        dag.AgGrid(
            columnDefs=columnDefs,
            rowData=df.to_dict("records"),
            defaultColDef=defaultColDef,
        ),
    ],
    style={"margin": 20},
)


if __name__ == "__main__":
    app.run_server(debug=True)
