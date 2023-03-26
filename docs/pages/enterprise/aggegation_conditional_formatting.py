from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description
from utils.other_components import enterprise_blurb


register_page(
    __name__,
    order=4,
    description=app_description,
    title="Dash AG Grid Enterprise Features",
)

text1 = """
# Row Aggregation with Conditional Formatting

This will style both the summary and detail level:

```
cellStyle = "cellStyle": {
    "styleConditions": [
        {"condition": "params.value > 100", "style": {"color": "red"}}
    ]
},
```

This will style the summary levels only:

```
cellStyle={
    "styleConditions": [
        {
            "condition": "params.node.aggData ? params.node.aggData.gold < 3 : false",
            "style": {"backgroundColor": "silver"},
        }
    ]
}
```

"""


layout = html.Div(
    [
        make_md(text1),
        make_md(enterprise_blurb),
        example_app("examples.enterprise.aggregation_conditional_formatting", make_layout=make_tabs),
        # up_next("text"),
    ],
)
