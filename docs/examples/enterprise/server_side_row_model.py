"""
Server-Side Row Model with Multi-Level Row Grouping

This example demonstrates the server-side row model with 3-level row grouping.
- Level 1: Countries (grouped)
- Level 2: Cities (grouped within countries)
- Level 3: Districts (leaf nodes within cities)
- Loads each level on demand when expanding a group
- Uses server-side row grouping with a single auto-group column

Note: This requires enableEnterpriseModules=True and a valid license key.
"""

import dash_ag_grid as dag
from dash import Dash, Input, Output, html, dcc
import time

app = Dash(__name__)

# Hierarchical data structure: Countries -> Cities -> Districts
# In a real application, this would come from a database
COUNTRIES_DATA = [
    {"id": "usa", "country": "United States", "population": 331000000},
    {"id": "uk", "country": "United Kingdom", "population": 67000000},
    {"id": "canada", "country": "Canada", "population": 38000000},
]

CITIES_DATA = {
    "usa": [
        {"id": "usa-nyc", "city": "New York", "population": 8400000},
        {"id": "usa-la", "city": "Los Angeles", "population": 4000000},
    ],
    "uk": [
        {"id": "uk-london", "city": "London", "population": 9000000},
        {"id": "uk-birmingham", "city": "Birmingham", "population": 1100000},
    ],
    "canada": [
        {"id": "canada-toronto", "city": "Toronto", "population": 2900000},
        {"id": "canada-vancouver", "city": "Vancouver", "population": 675000},
    ],
}

DISTRICTS_DATA = {
    "usa-nyc": [
        {"id": "usa-nyc-manhattan", "district": "Manhattan", "population": 1630000},
        {"id": "usa-nyc-brooklyn", "district": "Brooklyn", "population": 2560000},
        {"id": "usa-nyc-queens", "district": "Queens", "population": 2270000},
    ],
    "usa-la": [
        {"id": "usa-la-downtown", "district": "Downtown", "population": 52400},
        {"id": "usa-la-hollywood", "district": "Hollywood", "population": 153000},
        {"id": "usa-la-venice", "district": "Venice", "population": 37000},
    ],
    "uk-london": [
        {"id": "uk-london-westminster", "district": "Westminster", "population": 255000},
        {"id": "uk-london-camden", "district": "Camden", "population": 270000},
        {"id": "uk-london-tower", "district": "Tower Hamlets", "population": 310000},
    ],
    "uk-birmingham": [
        {"id": "uk-birm-centre", "district": "City Centre", "population": 25000},
        {"id": "uk-birm-edgbaston", "district": "Edgbaston", "population": 22000},
    ],
    "canada-toronto": [
        {"id": "canada-tor-downtown", "district": "Downtown", "population": 250000},
        {"id": "canada-tor-north", "district": "North York", "population": 670000},
        {"id": "canada-tor-scarbor", "district": "Scarborough", "population": 632000},
    ],
    "canada-vancouver": [
        {"id": "canada-van-downtown", "district": "Downtown", "population": 55000},
        {"id": "canada-van-westend", "district": "West End", "population": 45000},
    ],
}

app.layout = html.Div(
    [
        dcc.Markdown(
            """
            ## Server-Side Row Model with Multi-Level Row Grouping

            This example demonstrates:
            - **3-level hierarchy**: Countries -> Cities -> Districts
            - **Lazy loading** of grouped data at each level
            - **Level 1**: Countries (loaded initially)
            - **Level 2**: Cities (loaded when you expand a country)
            - **Level 3**: Districts (loaded when you expand a city)

            Click the arrows to drill down through the hierarchy.

            **Note:** Requires AG Grid Enterprise license
            """
        ),
        dag.AgGrid(
            id="server-side-hierarchy-grid",
            columnSize="sizeToFit",
            columnDefs=[
                {
                    "field": "country",
                    "rowGroup": True,
                    "hide": True,
                },
                {
                    "field": "city",
                    "rowGroup": True,
                    "hide": True,
                },
                {
                    "field": "population",
                    "headerName": "Population",
                },
            ],
            defaultColDef={"sortable": True},
            rowModelType="serverSide",
            enableEnterpriseModules=True,
            # licenseKey="YOUR_LICENSE_KEY_HERE",  # Uncomment and add your license key
            dashGridOptions={
                "autoGroupColumnDef": {
                    "headerName": "Location",
                    "field": "district",
                    "minWidth": 250,
                    "cellRendererParams": {
                        "suppressCount": True,
                    },
                },
                "cacheBlockSize": 100,
            },
        ),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("server-side-hierarchy-grid", "getRowsResponse"),
    Input("server-side-hierarchy-grid", "getRowsRequest"),
    prevent_initial_call=True,
)
def load_grouped_data(request):
    """
    Handle server-side data requests with 3-level row grouping support.

    The request contains:
    - groupKeys: Array indicating which group is being expanded
      - [] = root level (country groups)
      - ['United States'] = cities within United States
      - ['United States', 'New York'] = districts within New York
    - rowGroupCols: Array of columns being grouped
    """
    if not request:
        return None

    # Simulate server-side processing delay
    time.sleep(1)

    group_keys = request.get("groupKeys", [])

    # Level 1: Countries
    if len(group_keys) == 0:
        rows = [
            {
                "country": item["country"],
                "population": item["population"],
            }
            for item in COUNTRIES_DATA
        ]
        return {
            "rowData": rows,
            "rowCount": len(rows),
        }

    # Level 2: Cities for a specific country
    elif len(group_keys) == 1:
        country_name = group_keys[0]

        # Find the country ID from the name
        country_id = None
        for country in COUNTRIES_DATA:
            if country["country"] == country_name:
                country_id = country["id"]
                break

        if country_id and country_id in CITIES_DATA:
            cities = CITIES_DATA[country_id]
            rows = [
                {
                    "country": country_name,
                    "city": city["city"],
                    "population": city["population"],
                    "_cityId": city["id"],  # Store for later use
                }
                for city in cities
            ]
            return {
                "rowData": rows,
                "rowCount": len(rows),
            }

    # Level 3: Districts for a specific city
    elif len(group_keys) == 2:
        country_name = group_keys[0]
        city_name = group_keys[1]

        # Find the city ID
        country_id = None
        for country in COUNTRIES_DATA:
            if country["country"] == country_name:
                country_id = country["id"]
                break

        if country_id and country_id in CITIES_DATA:
            city_id = None
            for city in CITIES_DATA[country_id]:
                if city["city"] == city_name:
                    city_id = city["id"]
                    break

            if city_id and city_id in DISTRICTS_DATA:
                districts = DISTRICTS_DATA[city_id]
                rows = [
                    {
                        "country": country_name,
                        "city": city_name,
                        "district": district["district"],
                        "population": district["population"],
                    }
                    for district in districts
                ]
                return {
                    "rowData": rows,
                    "rowCount": len(rows),
                }

    # Default case
    return {
        "rowData": [],
        "rowCount": 0,
    }


if __name__ == "__main__":
    app.run(debug=True)
