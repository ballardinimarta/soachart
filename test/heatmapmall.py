import plotly.graph_objects as go
import datetime
import numpy as np
from test import testdata

servers = ['a.ns.se', 'b.ns.se', 'c.ns.se', 'f.ns.se', 'g.ns.se', 'i.ns.se', 'x.ns.se', 'y.ns.se', 'z.ns.se']

base = datetime.datetime.now()
time = base - np.arange(180) * datetime.timedelta(minutes=1)
z = testdata.data


fig = go.Figure(data=go.Heatmap(
    z=z,
    x=time,
    y=servers,
    colorscale='viridis',
    ygap=20,
    xgap=1,
    hovertemplate=
    "<b>'SOA zones for .se'</b><br><br>" +
    "Server: %{y}<br><br>" +
    "Time: %{x}<br><br>" +
    "Soa Zone: %{z}" +
    "<extra></extra>"
)
)
button_layer_1_height = 1.13
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(
                    args=["colorscale", "Viridis"],
                    label="Viridis",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Cividis"],
                    label="Cividis",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Blackbody"],
                    label="Blackbody",
                    method="restyle"
                ),
                dict(
                    args=["colorscale", "Jet"],
                    label="Jet",
                    method="restyle"
                ),
            ]),
        direction = "down",
                    pad = {"r": 10, "t": 10},
                          showactive = True,
                                       x = 0.07,
                                           xanchor = "left",
                                                     y = button_layer_1_height,
                                                         yanchor = "top"
        )])

fig.update_layout(
    title="SOA zones for .se",
    xaxis_nticks=36,
    xaxis_rangeslider=dict(visible=True),
    hoverlabel=dict(bgcolor='red', bordercolor='black'),
    plot_bgcolor='white',
    xaxis_title="Time",
    yaxis_title="Server",
    autosize=False,
    width=1250,
    height=600,
    margin=dict(t=100, b=0, l=0, r=0),
    font=dict(
        family="arial",
        size=13,
        color="Black"),
    annotations=[
            dict(text="colorscale:", x=0, xref="paper", y=1.08, yref="paper",
                                align="center", showarrow=False)]
)

fig.show()
