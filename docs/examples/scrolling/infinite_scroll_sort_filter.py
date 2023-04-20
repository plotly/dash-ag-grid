import dash_ag_grid as dag
from dash import Dash, Input, Output, dcc, html, no_update
import pandas as pd


app = Dash(__name__)

raw_data = {"id": [], "name": []}
for i in range(0, 10000):
    raw_data["id"].append(i)
    raw_data["name"].append(f"{i * 3 % 5}-{i * 7 % 15}-{i % 8}")

df = pd.DataFrame(data=raw_data)

app.layout = html.Div(
    [
        dcc.Markdown("Infinite scroll with sort and filter"),
        dag.AgGrid(
            id="infinite-sort-filter-grid",
            columnSize="sizeToFit",
            columnDefs=[
                {"field": "id", "filter": "agNumberColumnFilter"},
                {"field": "name"},
            ],
            defaultColDef={"sortable": True, "filter": True, "floatingFilter": True},
            rowModelType="infinite",
            dashGridOptions={
                # The number of rows rendered outside the viewable area the grid renders.
                "rowBuffer": 0,
                # How many blocks to keep in the store. Default is no limit, so every requested block is kept.
                "maxBlocksInCache": 1,
                "rowSelection": "multiple",
            },
        ),
    ],
    style={"margin": 20},
)

operators = {
    "greaterThanOrEqual": "ge",
    "lessThanOrEqual": "le",
    "lessThan": "lt",
    "greaterThan": "gt",
    "notEqual": "ne",
    "equals": "eq",
}


def filterDf(df, data, col):
    if data["filterType"] == "date":
        crit1 = data["dateFrom"]
        crit1 = pd.Series(crit1).astype(df[col].dtype)[0]
        if "dateTo" in data:
            crit2 = data["dateTo"]
            crit2 = pd.Series(crit2).astype(df[col].dtype)[0]
    else:
        crit1 = data["filter"]
        crit1 = pd.Series(crit1).astype(df[col].dtype)[0]
        if "filterTo" in data:
            crit2 = data["filterTo"]
            crit2 = pd.Series(crit2).astype(df[col].dtype)[0]
    if data["type"] == "contains":
        df = df.loc[df[col].str.contains(crit1)]
    elif data["type"] == "notContains":
        df = df.loc[~df[col].str.contains(crit1)]
    elif data["type"] == "startsWith":
        df = df.loc[df[col].str.startswith(crit1)]
    elif data["type"] == "notStartsWith":
        df = df.loc[~df[col].str.startswith(crit1)]
    elif data["type"] == "endsWith":
        df = df.loc[df[col].str.endswith(crit1)]
    elif data["type"] == "notEndsWith":
        df = df.loc[~df[col].str.endswith(crit1)]
    elif data["type"] == "inRange":
        if data["filterType"] == "date":
            df = df.loc[df[col].astype("datetime64[ns]").between_time(crit1, crit2)]
        else:
            df = df.loc[df[col].between(crit1, crit2)]
    elif data["type"] == "blank":
        df = df.loc[df[col].isnull()]
    elif data["type"] == "notBlank":
        df = df.loc[~df[col].isnull()]
    else:
        df = df.loc[getattr(df[col], operators[data["type"]])(crit1)]
    return df


@app.callback(
    Output("infinite-sort-filter-grid", "getRowsResponse"),
    Input("infinite-sort-filter-grid", "getRowsRequest"),
)
def infinite_scroll(request):
    dff = df.copy()

    if request:
        if request["filterModel"]:
            fils = request["filterModel"]
            for k in fils:
                try:
                    if "operator" in fils[k]:
                        if fils[k]["operator"] == "AND":
                            dff = filterDf(dff, fils[k]["condition1"], k)
                            dff = filterDf(dff, fils[k]["condition2"], k)
                        else:
                            dff1 = filterDf(dff, fils[k]["condition1"], k)
                            dff2 = filterDf(dff, fils[k]["condition2"], k)
                            dff = pd.concat([dff1, dff2])
                    else:
                        dff = filterDf(dff, fils[k], k)
                except:
                    pass
            dff = dff

        if request["sortModel"]:
            sorting = []
            asc = []
            for sort in request["sortModel"]:
                sorting.append(sort["colId"])
                if sort["sort"] == "asc":
                    asc.append(True)
                else:
                    asc.append(False)
            dff = dff.sort_values(by=sorting, ascending=asc)

        lines = len(dff.index)
        if lines == 0:
            lines = 1

        partial = dff.iloc[request["startRow"] : request["endRow"]]
        return {"rowData": partial.to_dict("records"), "rowCount": lines}


if __name__ == "__main__":
    app.run_server(debug=True)
