from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description


register_page(
    __name__,
    order=3,
    description=app_description,
    title="Dash AG Grid Components - Many components one row",

)

text1 = """
# Many Renderer Components One Column


It is also possible to use different renderers for different rows in the same column. To configure this set 
`cellRendererSelector` to a function that returns alternative values for `cellRenderer` and `cellRendererParams`.

In this example, we define the two components  in `dashAgGridComponentFunctions.js in the assets folder`
This will register the components and make them available to use in the grid.

```
var dagcomponentfuncs = (window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {});

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
```

Then we define the function to use with the `cellRendererSelector` in the `dashAgGridFunctions.js` folder.

```

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
```

### Example Two Cell Renderer components in one column

"""


layout = html.Div(
    [
        make_md(text1),
        example_app("examples.components.many_components_one_column", make_layout=make_tabs),

    ],
)
