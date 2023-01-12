from dash import html
import dash_design_kit as ddk


def enterprise_blurb():
    return html.Div(
        [
            ddk.Icon(icon_name="info-circle"),
            html.P(
                children=[
                    """
                    This feature requires the Enterprise version of AG Grid. See 
                    """,
                    html.A(
                        children="the AG Grid website",
                        href="https://www.ag-grid.com/license-pricing.php",
                    ),
                    """
                    for more information.
                    """,
                ],
                style={
                    "margin-right": "10px",
                    "margin-left": "10px",
                },
            ),
        ],
        style={
            "background-color": "var(--background_content)",
            "border-radius": "0.25rem",
            "display": "flex",
            "align-items": "center",
            "padding-left": "0.8rem",
        },
    )
