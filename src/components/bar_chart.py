import plotly.express as px
from dash import Dash, dcc, html
from dash.dependencies import Input, Output

import pandas as pd

from . import ids

# creating the DataFrame
MEDAL_DATA = px.data.medals_long()

def render(app: Dash) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.NATION_DROPDOWN, "value"),
        ],
    )

    def update_bar_chart(nations: list[str]) -> html.Div:
        filtered_data = MEDAL_DATA.query("nation in @nations")

        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")
        
        fig = px.bar(filtered_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)
    
    return html.Div(id=ids.BAR_CHART)

