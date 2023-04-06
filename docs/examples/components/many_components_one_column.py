from dash import Dash, dcc, html
import dash_ag_grid as dag

app = Dash(__name__)


rowData=[
        { 'value': 14, 'type': 'age' },
        { 'value': 'Female', 'type': 'gender' },
        { 'value': 'Happy', 'type': 'mood' },
        { 'value': 21, 'type': 'age' },
        { 'value': 'Male', 'type': 'gender' },
        { 'value': 'Sad', 'type': 'mood' },
      ]


columnDefs= [
    { 'field': 'value' },
    {
      'headerName': 'Rendered Value',
      'field': 'value',
      'cellRendererSelector': {'function': 'moodOrGender(params)'}
    },
    { 'field': 'type' },
  ]

defaultColDef={'flex': 1}

grid = dag.AgGrid(
    rowData=rowData,
    columnDefs=columnDefs,
    defaultColDef=defaultColDef,
    columnSize="sizeToFit",
)


app.layout = html.Div(
    [
        dcc.Markdown("This grid demonstrates one column with different renderer components in different rows."),
        grid
    ],
    style={"margin": 20},
)
if __name__ == "__main__":
    app.run_server(debug=True)


"""


----------------------
// Place the following in the dashAgGridComponents.js file in the assets folder


dagcomponentfuncs.MoodRenderer = function (props) {
    const imgForMood = 'https://www.ag-grid.com/example-assets/smileys/' + (props.value === 'Happy' ? 'happy.png' : 'sad.png')
    
    return React.createElement(
        'img',
        {src: imgForMood, width: "20px"},
    );
}

dagcomponentfuncs.GenderRenderer = function (props) {
    const image = this.props.value === 'Male' ? 'male.png' : 'female.png';
    const imageSource = `https://www.ag-grid.com/example-assets/genders/${image}`;
    return React.createElement(
        'img',
        {src: imageSource, width: "20px"},
    );
}

-----------------------------------------
// Place the following in the dashAgGridFunctions.js file in the assets folder

var dagfuncs = window.dashAgGridFunctions = window.dashAgGridFunctions || {};

dagfuncs.moodOrGender = function (params) {
  var dagcomponentfuncs = window.dashAgGridComponentFunctions
           const moodDetails = {
              component: dagcomponentfuncs.MoodRenderer,
            };
            const genderDetails = {
              component: dagcomponentfuncs.GenderRenderer,
              params: { values: ['Male', 'Female'] },
            };
            if (params.data) {
              if (params.data.type === 'gender') return genderDetails;
              else if (params.data.type === 'mood') return moodDetails;
            }
            return undefined;
}
"""