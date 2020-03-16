import plotly.graph_objects as go
import datetime
from listcreate import all_soa_list, unique, all_time_list, timelist
import numpy as np

for i in all_soa_list:
    i.sort()

# Define z, x and y values
servers = ['a.ns.se', 'b.ns.se', 'c.ns.se', 'f.ns.se', 'g.ns.se', 'i.ns.se','x.ns.se', 'y.ns.se', 'z.ns.se']
time = timelist
z = all_soa_list

# Creating plot, making a custom hovertemplate for the hovertext and editing the colorbar
fig = go.Figure(data=go.Heatmap(
    z=z,
    x=time,
    y=servers,
    ygap=10,
    colorscale='viridis',
    xgap=0,
    hovertemplate=
    "<b>'SOA zones for .se'</b><br><br>" +
    "Server: %{y}<br><br>" +
    "Time: %{x}<br><br>" +
    "Soa Zone: %{z:" "}" +
    "<extra></extra>",
    colorbar=dict(
        showtickprefix="none",
        thickness=15,
        tickformat=" ",
        tickmode = 'array',
        tickvals = unique,
        ticktext= unique,
        )
)
)
# Updating some layout values
fig.update_layout(
    title="SOA zones for .se",
    hoverlabel=dict(bgcolor='green', bordercolor='black'),
    plot_bgcolor='white',
    xaxis=dict(
        title="Time",
        rangeslider=dict(visible=True, thickness=0.10)
    ),
    yaxis=dict(
        title="Server",
        autorange='reversed'
    ),
    autosize=True,
    font=dict(
        family="arial",
        size=13,
        color="Black"))
# Display the plot
fig.show()
