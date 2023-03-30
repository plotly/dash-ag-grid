"""
styling with custom cell renderer

Note:
Custom components  must be defined in the dashAgGridComponentFunctions.js in assets folder.
"""


import dash_ag_grid as dag
from dash import Dash, html, dcc, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc

webb_stephans_quintet = "https://user-images.githubusercontent.com/72614349/179115663-71578706-1ab5-45a5-b809-812c7c3028a7.jpg"
webb_deep_field = "https://user-images.githubusercontent.com/72614349/179115668-2630e3e4-3a9f-4c88-9494-3412e606450a.jpg"
webb_southern_nebula = "https://user-images.githubusercontent.com/72614349/179115670-ef5bc561-d957-4e88-82dc-53ca53541b04.jpg"
webb_carina = "https://user-images.githubusercontent.com/72614349/179115673-15eaccb9-d17d-4667-84fb-e0a46fd444e8.jpg"


data_dict = {
    "name": ["Deep Field", "Southern Nebula", "Stephans Quintet", "Carina Nebula"],
    "img": [webb_deep_field, webb_southern_nebula, webb_stephans_quintet, webb_carina],
    "more_info": [
        "[James Webb Space Telescope First Images](https://www.nasa.gov/image-feature/goddard/2022/nasa-s-webb-delivers-deepest-infrared-image-of-universe-yet)",
        "[JWST -A dying star](https://www.nasa.gov/image-feature/goddard/2022/nasa-s-webb-captures-dying-star-s-final-performance-in-fine-detail)",
        "[JWST - Galexy evolution and black holes](https://www.nasa.gov/image-feature/goddard/2022/nasa-s-webb-sheds-light-on-galaxy-evolution-black-holes)",
        "[JWST Birth of a star](https://www.nasa.gov/image-feature/goddard/2022/nasa-s-webb-reveals-cosmic-cliffs-glittering-landscape-of-star-birth)",
    ],
}
df = pd.DataFrame(data_dict)

columnDefs = [
    {
        "headerName": "Thumbnail",
        "field": "img",
        "cellRenderer": "ImgThumbnail",
        "width": 100,
    },
    {
        "headerName": "Image Name",
        "field": "name",
    },
    {"headerName": "More Info", "field": "more_info", "cellRenderer": "markdown"},
]


grid = dag.AgGrid(
    id="custom-component-img-grid",
    columnDefs=columnDefs,
    rowData=df.to_dict("records"),
    dashGridOptions={"rowHeight": 100},
    style={"height": 475},
    columnSize="sizeToFit",
)


app = Dash(__name__, external_stylesheets=[dbc.themes.SPACELAB])

app.layout = html.Div(
    [
        dcc.Markdown(
            "Example of cellRenderer with custom Image component. Click on Thumbnail to see full size Image"
        ),
        grid,
        dbc.Modal(id="custom-component-img-modal", size="xl"),
    ],
    style={"margin": 20},
)


@app.callback(
    Output("custom-component-img-modal", "is_open"),
    Output("custom-component-img-modal", "children"),
    Input("custom-component-img-grid", "cellRendererData"),
)
def show_change(data):
    if data:
        return True, html.Img(src=data["value"])
    return False, None


if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put the following in the dashAgGridComponentFunctions.js file in the assets folder


---------------

var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};


dagcomponentfuncs.ImgThumbnail = function (props) {
    const {setData, data} = props;

    function onClick() {
        setData(props.value);
    }

    return React.createElement(
        'div',
        {
            style: {
                width: '100%',
                height: '100%',
                display: 'flex',
                alignItems: 'center',
            },
        },
        React.createElement(
            'img',
            {
                onClick: onClick,
                style: {width: '100%', height: 'auto'},
                src: props.value,

            },
        )
    );
};

"""
