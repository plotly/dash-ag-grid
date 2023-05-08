
"""
Reminder - In dcc.Markdown, be sure to use dcc.Link when linking to other pages in the app

`dcc.Markdown( "This is text <dccLink href='page1/news' children='Page 1' /> more text", dangerously_allow_html=True)`
"""




from dash import dcc, html
import dash_bootstrap_components as dbc

icon_left = html.I(className="fa-solid fa-hand-point-left fs-5 me-2")
icon_up = html.I(className="fa-solid fa-hand-point-up fs-5 me-2")
icon_info = html.I(className="fa-solid fa-info-circle me-2")


def make_link(text, icon, link):
    return html.Span(html.A([html.I(className=icon + " ps-1 pe-2"), text], href=link))


def up_next(text):
    return dcc.Markdown(
        text,
        className="m-5 px-3 dbc",
        dangerously_allow_html=True,
    )


def make_md(text, className="mt-5"):
    return html.Div(dcc.Markdown(
        text, className="mx-5 px-3", dangerously_allow_html=True, link_target="_blank",
        style={"maxWidth": 1000}
    ),className=className)


enterprise_blurb = """
> This feature requires the Enterprise version of AG Grid. See the [AG Grid website](https://www.ag-grid.com/license-pricing.php) for more information.
"""


def make_feature_card(img, txt):
    return dbc.Card(
        [dbc.CardBody(dcc.Markdown(txt)), dbc.CardImg(src=img)],
        className="shadow my-5 mx-5 px-3",
        style={"maxWidth": 1000},
    )





import re


def ComponentReference(component_name, lib=dcc):
    component = getattr(lib, component_name)
    component_doc = component.__doc__

    return_div = [
        dcc.Markdown(
            f"""
            > Access this documentation in your Python terminal with:
            > ```python
            > >>> help({lib.__name__}.{component_name})
            > ```
            """
        )
    ]

    docs = component_doc.split("Keyword arguments:")[-1]


    # formats code blocks that includes square brackets
    docs = docs.replace("[", "\[").replace("]", "\]")
    verbatim_regex = r"`((\\\[)((.|\n)*?)(\\\]))`"
    docs = re.sub(re.compile(verbatim_regex), r"`[\3]`", docs)

    # format links
    link_regex = r"\\\[([\w\.\-:\s\/]+)\\\]\(([\w\.\-:#\/]+)\)"
    docs = re.sub(re.compile(link_regex), r"[\1](\2)", docs)

    # formats the prop defaults
    prop_optional_default_regex = r"""default (.*)\)"""
    docs = re.sub(re.compile(prop_optional_default_regex), r"default `\1`)", docs)

    # formats the prop type
    prop_type_regex = r"""(\s*- \w+?\s*\()([^;]*);"""
    docs = re.sub(re.compile(prop_type_regex), r"\1*\2*;", docs)

    # formats the prop name on first level only
    prop_name_regex = r"""(\n- )(\w+?) \("""
    docs = re.sub(re.compile(prop_name_regex), r"\1**`\2`** (", docs)

    # formats keys of nested dicts
    nested_prop_name_regex = r"""(\n\s+- )(\w+?) \("""
    docs = re.sub(re.compile(nested_prop_name_regex), r"\1**`\2`** (", docs)

    # removes a level of nesting
    docs = docs.replace("\n-", "\n")

    return_div.append(dcc.Markdown(docs))
    return html.Div(return_div, className="mx-5 px-3", style={"maxWidth": 1000})

