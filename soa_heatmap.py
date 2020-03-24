import plotly.graph_objects as go
from listcreate import all_soa_list, all_dt_list, timelist, ticktext, tickvals


# Sorting soa values
for i in all_soa_list:
    i.sort()

# Define z, x, y and customdata values
servers = ['a.ns.se', 'b.ns.se', 'c.ns.se', 'f.ns.se', 'g.ns.se', 'i.ns.se', 'm.ns.se', 'x.ns.se', 'y.ns.se', 'z.ns.se']
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
    hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{customdata}<br><br>" +
    "<extra></extra>",
    colorbar=dict(
        title='<b>SOA Zone<b>',
        tickfont=dict(
        family="arial",
        size=10,
        color="black"),
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
    title="SOA zones for .se secondary name servers",
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
        color="black"),
    hoverlabel= dict(
        bgcolor='Black'
    )
    )
# Display the plot
fig.show()

# Write HTML file
#fig.write_html("path/to/file.html")
