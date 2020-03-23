import plotly.graph_objects as go
import datetime
from listcreate import unique, all_soa_list, all_dt_list, timelist, all_time_list, ticktext, tickvals
import numpy as np
for i in all_soa_list:
    i.sort()

hov = ticktext
colorvals=np.array(list(range(len(unique))))
# Define z, x and y values
servers = ['a.ns.se', 'b.ns.se', 'c.ns.se', 'f.ns.se', 'g.ns.se', 'i.ns.se', 'm.ns.se', 'x.ns.se', 'y.ns.se', 'z.ns.se']
z = all_soa_list
time = timelist
custom = all_time_list

# Creating plot, making a custom hovertemplate for the hovertext and editing the colorbar
fig = go.Figure(data=go.Heatmap(
    z=all_soa_list,
    x=timelist,
    y=servers,
    customdata=custom,
    ygap=10,
    colorscale='portland',
    xgap=0,
    hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{customdata}<br><br>" +
    "<b>Soa Zone:</b> %{}" +
    "<extra></extra>",
    colorbar=dict(
        showtickprefix="none",
        thickness=15,
        tickmode='array',
        tickvals=tickvals,
        ticktext=ticktext,
    )
)
)
# Updating some layout values
fig.update_layout(
    template="ggplot2",
    title="SOA zones for .se",
    plot_bgcolor='white',
    xaxis=dict(
        title="Time",
        rangeslider=dict(visible=True, thickness=0.10),
        rangeselector=dict(
            buttons=list([
                dict(count=30,
                     label="30 min",
                     step="minute",
                     stepmode="backward"),
                dict(count=1,
                     label="1 hour",
                     step="hour",
                     stepmode="backward"),
                dict(count=2,
                     label="2 hour",
                     step="hour",
                     stepmode="backward"),
                dict(count=3,
                     label="3 hour",
                     step="hour",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
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
#fig.write_html('/Users/marta.ballardini/Desktop/plot.html')
    #("path/to/file.html")
