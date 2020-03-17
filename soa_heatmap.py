import plotly.graph_objects as go
import datetime
from listcreate import unique, all_soa_list, all_dt_list, timelist
import numpy as np
for i in all_soa_list:
    i.sort()

# Define z, x and y values
servers = ['a.ns.se', 'b.ns.se', 'c.ns.se', 'f.ns.se', 'g.ns.se', 'i.ns.se','x.ns.se', 'y.ns.se', 'z.ns.se']
z = all_soa_list
time = timelist
custom = all_dt_list

# Creating plot, making a custom hovertemplate for the hovertext and editing the colorbar
fig = go.Figure(data=go.Heatmap(
    z=z,
    x=time,
    y=servers,
    customdata=custom,
    ygap=10,
    colorscale='portland',
    xgap=0,
    hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{customdata}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
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
    template="ggplot2",
    title="SOA zones for .se",
    hoverlabel=dict(bgcolor='black', bordercolor='black',font=dict(
        family="arial",
        color="white")
    ),
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
        color="black")
    )
# Display the plot
fig.show()

# Write HTML file
#fig.write_html("path/to/file.html")
