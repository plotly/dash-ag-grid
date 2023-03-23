"""
Nested tables.
"""

import dash_ag_grid as dag
import dash
from dash import Input, Output, html, dcc, Dash, no_update
from . import utils
import pandas as pd
from dash.testing.wait import until
import time

def test_is001_infinite_scroll(dash_duo):
    app = Dash(__name__)

    raw_data = {"id": [], "name": []}
    for i in range(0, 10000):
        raw_data["id"].append(i)
        raw_data["name"].append(f"{i * 3 % 5}-{i * 7 % 15}-{i % 8}")

    df = pd.DataFrame(data=raw_data)

    app.layout = html.Div(
        [
            dag.AgGrid(
                id="grid",

                columnSize="sizeToFit",
                columnDefs=[{"field": "id", 'filter': 'agNumberColumnFilter'}, {"field": "name"}],
                defaultColDef={"sortable": True, "filter": True, "floatingFilter": True},
                rowModelType="infinite",
                dashGridOptions={
                    # The number of rows rendered outside the viewable area the grid renders.
                    "rowBuffer": 0,
                    # How many blocks to keep in the store. Default is no limit, so every requested block is kept.
                    "maxBlocksInCache": 1,
                    "rowSelection": "multiple",
                }
            )
        ]
    )

    operators = {
        'greaterThanOrEqual': 'ge',
        'lessThanOrEqual': 'le',
        'lessThan': 'lt',
        'greaterThan': 'gt',
        'notEqual': 'ne',
        'equals': 'eq'
    }

    def filterDf(df, data, col):
        if data['filterType'] == 'date':
            crit1 = data['dateFrom']
            crit1 = pd.Series(crit1).astype(df[col].dtype)[0]
            if 'dateTo' in data:
                crit2 = data['dateTo']
                crit2 = pd.Series(crit2).astype(df[col].dtype)[0]
        else:
            crit1 = data['filter']
            crit1 = pd.Series(crit1).astype(df[col].dtype)[0]
            if 'filterTo' in data:
                crit2 = data['filterTo']
                crit2 = pd.Series(crit2).astype(df[col].dtype)[0]
        if data['type'] == 'contains':
            df = df.loc[df[col].str.contains(crit1)]
        elif data['type'] == 'notContains':
            df = df.loc[~df[col].str.contains(crit1)]
        elif data['type'] == 'startsWith':
            df = df.loc[df[col].str.startswith(crit1)]
        elif data['type'] == 'notStartsWith':
            df = df.loc[~df[col].str.startswith(crit1)]
        elif data['type'] == 'endsWith':
            df = df.loc[df[col].str.endswith(crit1)]
        elif data['type'] == 'notEndsWith':
            df = df.loc[~df[col].str.endswith(crit1)]
        elif data['type'] == 'inRange':
            if data['filterType'] == 'date':
                df = df.loc[df[col].astype('datetime64[ns]').between_time(crit1, crit2)]
            else:
                df = df.loc[df[col].between(crit1, crit2)]
        elif data['type'] == 'blank':
            df = df.loc[df[col].isnull()]
        elif data['type'] == 'notBlank':
            df = df.loc[~df[col].isnull()]
        else:
            df = df.loc[getattr(df[col], operators[data['type']])(crit1)]
        return df

    @app.callback(
        Output("grid", "getRowsResponse"),
        Input("grid", "getRowsRequest")
    )
    def infinite_scroll(request):
        dff = df.copy()

        if request:
            if request['filterModel']:
                fils = request['filterModel']
                for k in fils:
                    try:
                        if 'operator' in fils[k]:
                            if fils[k]['operator'] == 'AND':
                                dff = filterDf(dff, fils[k]['condition1'], k)
                                dff = filterDf(dff, fils[k]['condition2'], k)
                            else:
                                dff1 = filterDf(dff, fils[k]['condition1'], k)
                                dff2 = filterDf(dff, fils[k]['condition2'], k)
                                dff = pd.concat([dff1, dff2])
                        else:
                            dff = filterDf(dff, fils[k], k)
                    except:
                        pass
                dff = dff

            if request['sortModel']:
                sorting = []
                asc = []
                for sort in request['sortModel']:
                    sorting.append(sort['colId'])
                    if sort['sort'] == 'asc':
                        asc.append(True)
                    else:
                        asc.append(False)
                dff = dff.sort_values(by=sorting, ascending=asc)

            lines = len(dff.index)
            if lines == 0:
                lines = 1

            partial = dff.iloc[request["startRow"]: request["endRow"]]
            return {"rowData": partial.to_dict("records"), "rowCount": lines}

    dash_duo.start_server(app)

    grid = utils.Grid(dash_duo, "grid")
    grid.wait_for_cell_text(0, 0, "0")


    ## testing filtering with responses
    grid.set_filter(0, "1001")
    grid.wait_for_cell_text(0, 0, "1001")
    grid.set_filter(0, "")
    grid.wait_for_cell_text(0, 0, "0")

    ## testing sorting with responses
    grid.get_header_cell(0).click()
    grid.wait_for_cell_text(0, 0, "0")
    grid.get_header_cell(0).click()
    grid.wait_for_cell_text(0, 0, "9999")
    grid.get_header_cell(1).click()
    grid.wait_for_cell_text(1, 0, "3600")
    grid.get_header_cell(1).click()
    grid.wait_for_cell_text(0, 0, "7263")
