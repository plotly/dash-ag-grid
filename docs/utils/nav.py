"""
This is a collection of nav components and headers

"""
import dash
from dash import html
import dash_bootstrap_components as dbc


# Links
plotly_logo = "https://user-images.githubusercontent.com/72614349/182969599-5ae4f531-ea01-4504-ac88-ee1c962c366d.png"
plotly_logo_dark = "https://user-images.githubusercontent.com/72614349/182967824-c73218d8-acbf-4aab-b1ad-7eb35669b781.png"
plotly_ddk_url = "https://plotly.com/dash/design-kit/"
aggrid_logo = "https://user-images.githubusercontent.com/72614349/211098297-c208fed6-6bda-4f1d-8506-3051e1a8ec07.png"
aggrid_docs_url = "https://www.ag-grid.com/react-data-grid/"

examples_index_url = "https://dash-example-index.herokuapp.com/"
dash_docs_url = "https://dash.plotly.com/"
dash_forum_url = "https://community.plotly.com/"


def make_header(text, spacing="mt-4"):
    return html.H2(
        text,
        className="text-white bg-primary p-2 " + spacing,
    )


navbar = dbc.NavbarSimple(
    [
        html.A(
            html.Img(src=plotly_logo, height=50, className="m-2 shadow rounded"),
            href=dash_docs_url,
            target="blank",
            title="Plotly",
        ),
        html.A(
            html.Img(src=aggrid_logo, height=50, className="m-2 shadow rounded"),
            href=aggrid_docs_url,
            target="blank",
            title="Plotly",
        ),
    ],
    brand="Dash AG Grid",
    #  brand_href=dash.get_relative_path("/"),
    brand_href="/",
    color="primary",
    dark=True,
    fixed="top",
    className="mb-2  position-relative",
    style={"minWidth": 800},
)


def make_sidebar_category(category="/", title=""):
    include_home = category == "/getting-started"
    return dbc.AccordionItem(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"]),
                    ],
                    href=page["path"],
                    active="exact",
                    className="py-1",
                )
                for page in dash.page_registry.values()
                if page["path"].startswith(category)
                or (page["path"] == "/" and include_home)
            ],
            vertical=True,
            pills=True,
        ),
        title=title,
        item_id=category,
    )


def make_sidebar_category_hash(page, title):
    """
    Use this to create an accordion item with links containing hashtags to scroll to a positions on the page.
    when registering the page include a list of ids to scroll to in a `hashtags` prop


    Args:
        page: A page in the dash.page_registry
        title: The title to show as the Accordion label

    Returns: navlinks with hashtags.

    Example
        dbc.Nav(dbc.NavLink("position", href="/adding-themes/bootstrap-utility-classes#position", external_link=True)),
    """
    return dbc.AccordionItem(
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        tag,
                    ],
                    href=f"{page['path']}#{tag}",
                    external_link=True,  # must be true for scroll to work
                    active="exact",
                    className="py-1",
                )
                for tag in page.get("hashtags")
            ],
            vertical=True,
            pills=True,
        ),
        title=title,
    )


# TODO - refactor this if not using hashtags
def make_side_nav():
    return html.Div(
        [
            dbc.Accordion(
                [
                    make_sidebar_category(
                        category="/getting-started", title="Getting Started"
                    ),
                    make_sidebar_category(category="/columns", title="Columns"),
                    make_sidebar_category(category="/rows", title="Rows"),
                    make_sidebar_category(category="/layout", title="Layout & Style"),
                    make_sidebar_category(category="/selection", title="Selection"),
                    make_sidebar_category(category="/rendering", title="Rendering"),
                    make_sidebar_category(category="/editing", title="Editing"),
                    make_sidebar_category(
                        category="/import-export", title="Import & Export"
                    ),
                    make_sidebar_category(category="/components", title="Components"),
                    make_sidebar_category(
                        category="/enterprise", title="Enterprise Features"
                    ),
                    make_sidebar_category(
                        category="/other-examples", title="Other Examples"
                    ),
                ],
                flush=True,
                always_open=True,
                id="sidebar",
            ),
            # example of a category with hash tags
            # dbc.Accordion(
            #     [
            #         make_sidebar_category_hash(
            #             page=dash.page_registry["pages.bootstrap_utility_classes.bootstrap_utility_classes"],
            #             title="Bootstrap Utility Classes"
            #         )
            #     ],
            #
            # ),
        ],
        className="sticky-top vh-100 overflow-scroll",
    )
