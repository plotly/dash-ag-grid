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


def make_md(text):
    return dcc.Markdown(
        text, className="mx-5 px-3", dangerously_allow_html=True, link_target="_blank"
    )


enterprise_blurb = """
> This feature requires the Enterprise version of AG Grid. See the [AG Grid website](https://www.ag-grid.com/license-pricing.php) for more information.
"""
