from dash import html, register_page
from utils.code_and_show import example_app, make_tabs
from utils.other_components import up_next, make_md
from utils.utils import app_description

register_page(
    __name__,
    order=1,
    description=app_description,
    title="Dash AG Grid Rendering",
    # name="Bootstrap Utility Classes",
    # hashtags=["intro","background", "border", "color", "spacing", "text", "position"],
)

text1 = """
# Change Cell Renderers
The grid provides two cell renderers for animating changes to data. They are:

- `agAnimateShowChangeCellRenderer`: The previous value is temporarily shown beside the old value with a directional arrow showing increase or decrease in value. The old value is then faded out.
- `agAnimateSlideCellRenderer`: The previous value shown in a faded fashion and slides, giving a ghosting effect as the old value fades and slides away.

Example
The example below shows the `agAnimateShowChangeCellRenderer` To test, try the following:

Columns A,  and B are editable.
Columns C is updated via clicking the button.
Changes to any of the first 3 columns results in animations in the Total and Average column.

"""

layout = html.Div(
    [
        make_md(text1),
        example_app("examples.rendering.animation_renderer", make_layout=make_tabs),
        # up_next("text"),
    ],
)
