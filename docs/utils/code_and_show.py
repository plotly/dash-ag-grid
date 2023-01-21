import uuid
from dash import html, dcc
import dash_bootstrap_components as dbc
from utils.utils import example_source_codes, example_apps


def make_code_div(code):
    """
    Display code str in dcc.Markdown with dcc.Clipboard
    """

    # make a unique id for clipboard
    clipboard_id = str(uuid.uuid4())

    clipboard_style = {
        "right": 0,
        "position": "absolute",
        "top": 0,
        "backgroundColor": "#f6f6f6",
        "color": "#2f3337",
        "padding": 4,
    }
    return html.Div(
        [
            dcc.Markdown(f"```python\n{code}```\n"),
            dcc.Clipboard(
                target_id=f"{clipboard_id}",
                style=clipboard_style,
            ),
        ],
        id=f"{clipboard_id}",
        style={"position": "relative"},
    )


def example_app(
    filename,
    make_layout=None,
    run=True,
    show_code=True,
    notes=None,
    notes_first=None,
    image=None,
):
    """
    Creates the "code and show layout for an example dash app.

    - `filename`:
       The path to the file with the sample app code.

    - `make_layout`:
        A function which takes as attributes the code string and the live app and returns a
        layout.  The default layout displays the code side-by-side with the live app on large screens
        or app first followed by the code on smaller screens.

    - `run`:
        bool (default: True) Whether to run the app

    - `show_code`:
        bool (default: True) Whether to show the code

    - `notes`:
        str (default: None)  Notes or tutorial to display with the app.  Text may include markdown formatting
        as it will be displayed in a dcc.Markdown component

    - `image`:
         str (default: None) passed to the `src` prop of `html.Img(src=image)`

    """

    code = example_source_codes[filename]
    run_app = example_apps[filename].layout if run else ""

    # Removes the id prefix
    code = code.replace(filename + "-x-", "")
    code = code if show_code else ""

    if make_layout is not None:
        return make_layout(code, run_app, show_code, notes, notes_first, image)
    return make_side_by_side(code, run_app, notes, notes_first)


def make_side_by_side(code, show_app, notes, notes_first):
    """
    This is the default layout for the "code and show"
    It displays the app and the code side-by-side on large screens, or
    the app first, followed by the code on smaller screens.
    It also has a dcc.Clipboard to copy the code.  Notes will display
    in a dcc.Markdown component
    """

    return dbc.Row(
        [
            dcc.Markdown(
                notes_first,
                className="mb-4",
                link_target="_blank",
                dangerously_allow_html=True,
            )
            if notes_first
            else None,
            dbc.Col(dbc.Card(show_app, style={"padding": "10px"}), width=12, xl=6)
            if show_app
            else None,
            dbc.Col(
                dbc.Card(
                    [make_code_div(code)],
                    style={"max-height": "600px", "overflow": "auto"},
                ),
                width=12,
                xl=6,
            )
            if code != ""
            else None,
            dcc.Markdown(
                notes,
                className="m-4",
                link_target="_blank",
                dangerously_allow_html=True,
            )
            if notes
            else None,
        ],
        className="p-4",
    )


def make_app_first(code, show_app, show_code, notes, notes_first):
    """
    This is an alternate layout for the "code and show"
    It displays the app on top and the code below.
    This function can be used as an example of how to create your own custom layouts
    to be used with example_app() .

    Use this layout instead of the default by passing this function
    to the `make_layout` attribute in example_app()   e.g.:
    `example_app("pathto/my_filename.py", make_layout=make_app_first)`
    """

    return dbc.Row(
        [
            dcc.Markdown(
                notes_first,
                className="mb-4",
                link_target="_blank",
                dangerously_allow_html=True,
            )
            if notes_first
            else None,
            dbc.Col(dbc.Card(show_app, style={"padding": "10px"}), width=12)
            if show_app
            else None,
            dbc.Col(
                dbc.Card(
                    [make_code_div(code)],
                    style={"height": "700px", "overflow": "auto"},
                ),
                width=12,
            )
            if code
            else None,
            dcc.Markdown(
                notes,
                className="mt-4",
                link_target="_blank",
                dangerously_allow_html=True,
            )
            if notes
            else None,
        ],
        className="p-4",
    )


def make_tabs(code, show_app, show_code, notes, notes_first, image):
    """
    This shows the app with the code in a tab
    It displays the app and the code side-by-side on large screens, or
    the app first, followed by the code on smaller screens.
    It also has a dcc.Clipboard to copy the code.  Notes will display
    in a dcc.Markdown component.
    """

    # make a unique id for tabs
    tabs_id = "tabs" + str(uuid.uuid4())

    if image:
        tabs = dbc.Tabs(
            [
                dbc.Tab(
                    html.Img(src=image, className="img-fluid"),
                    label="Image",
                    className="p-4",
                ),
                dbc.Tab(
                    show_app,
                    label="Run App",
                    className="p-4",
                ),
                dbc.Tab(
                    make_code_div(code),
                    label="View Code",
                    className="p-4",
                ),
            ],
            id=tabs_id,
        )
    else:
        tabs = dbc.Tabs(
            [
                dbc.Tab(
                    show_app,
                    label="Run App",
                    className="p-4",
                ),
                dbc.Tab(
                    make_code_div(code),
                    label="View Code",
                    className="p-4",
                ),
            ],
            id=tabs_id,
        )
    return dbc.Row(
        dbc.Col(
            [
                dcc.Markdown(
                    notes_first,
                    className="mb-4",
                    link_target="_blank",
                    dangerously_allow_html=True,
                )
                if notes_first
                else None,
                tabs,
                dcc.Markdown(
                    notes,
                    className="m-4",
                    link_target="_blank",
                    dangerously_allow_html=True,
                )
                if notes
                else None,
            ],
            className="p-4",
        ),
        className="border shadow m-4",
    )
