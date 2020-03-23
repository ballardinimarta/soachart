import plotly.graph_objects as go
from plotly.subplots import make_subplots
from listcreate import unique
from parser import atime, asoa, btime, bsoa, csoa, ctime, fsoa, ftime, gsoa, gtime, isoa, itime, xsoa, xtime, ysoa,\
    ytime, zsoa, ztime,some_soa_list, some_time_list

fig = make_subplots(9,1, shared_xaxes=True)

fig.add_trace(
 go.Heatmap(x = atime, z = asoa, y=['a.ns.se'],coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"), 1,1)

fig.add_trace(
 go.Heatmap(x = btime, z = bsoa,y = ['b.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),2,1)

fig.add_trace(
 go.Heatmap(x = ctime, z = csoa,y = ['c.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),3,1)

fig.add_trace(
 go.Heatmap(x = ftime, z = fsoa,y = ['f.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),4,1)

fig.add_trace(
 go.Heatmap(x = gtime, z = gsoa,y = ['g.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),5,1)

fig.add_trace(
 go.Heatmap(x = itime, z = isoa,y = ['i.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),6,1)

fig.add_trace(
 go.Heatmap(x = xtime, z = xsoa,y = ['x.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),7,1)

fig.add_trace(
 go.Heatmap(x = ytime, z = ysoa,y = ['y.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),8,1)

fig.add_trace(
 go.Heatmap(x = ztime, z = zsoa,y = ['z.ns.se'], coloraxis = "coloraxis", hovertemplate=
    "<b>SOA zones for .se</b><br><br>" +
    "<b>Server:</b> %{y}<br><br>" +
    "<b>Time:</b> %{x}<br><br>" +
    "<b>Soa Zone:</b> %{z:" "}" +
    "<extra></extra>"),9,1)

fig.update_layout(
    coloraxis = dict(colorscale='viridis',
    colorbar=dict(
        showtickprefix="none",
        thickness=15,
        tickformat="",
        tickmode='array',
        tickvals=unique,
        ticktext=list(range(len(unique))))
    ),
    xaxis=dict(
        tickformat=""
    ),
    hoverlabel=dict(bgcolor='black', bordercolor='black', font=dict(
        family="arial",
        color="white")
                    )
)

fig.show()
