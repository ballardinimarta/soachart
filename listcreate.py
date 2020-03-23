from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.sagan import DnsResult
from measurements import kwargs_a, kwargs_b, kwargs_c, kwargs_f, kwargs_g, kwargs_i, kwargs_x, kwargs_y, kwargs_z
import datetime
import numpy as np


# Function that parses the results for a measurement and puts the soaserial and timestamp in 2 lists and then an
# additional list for the timestamps in datetimeformat and then returns those lists
def create_list(kwargs):
    is_success, results = AtlasResultsRequest(**kwargs).create()
    if is_success:
        l_soa = []
        l_time = []
        l_dt = []
        count = 0
        while count < len(results)-1:
            my_error = DnsResult(results[count])
            if not my_error.is_error:
                timestamp = results[count]['timestamp']
                dt = datetime.datetime.fromtimestamp(timestamp)
                #dt = dt.strftime("%m/%d/%Y , %H:%M:%S")
                soa_serial = results[count]['result']['answers'][0]['SERIAL']
                l_soa.append(soa_serial)
                l_time.append(timestamp)
                l_dt.append(dt)
            count += 1
        return l_soa, l_time, l_dt


# Create a time list, soa list and datetime list for each measurement
a = create_list(kwargs_a)
b = create_list(kwargs_b)
c = create_list(kwargs_c)
f = create_list(kwargs_f)
g = create_list(kwargs_g)
i = create_list(kwargs_i)
x = create_list(kwargs_x)
y = create_list(kwargs_y)
z = create_list(kwargs_z)

# Making a combined time/soa/datetime list for all servers
all_soa_list = [a[0], b[0], c[0], f[0], g[0], i[0], x[0], y[0], z[0]]
all_time_list = [a[1], b[1], c[1], f[1], g[1], i[1], x[1], y[1], z[1]]
all_dt_list = [a[2], b[2], c[2], f[2], g[2], i[2], x[2], y[2], z[2]]

# Setting colorbar tick values
for item in all_soa_list:
    unique = np.unique(item)

# Setting average datetime values
for s in all_time_list:
    s.sort()
av = [float(sum(l)) / len(l) for l in zip(*all_time_list)]
timelist = []
for count in av:
    dt = datetime.datetime.fromtimestamp(count)
    timelist.append(dt)

# colorscale colors
colorscale = [
    [0, 'red'],
    [0.14285714285, 'red'],
    [0.14285714285, 'green'],
    [0.28571428571, 'green'],
    [0.28571428571, 'blue'],
    [0.42857142857, 'blue'],
    [0.42857142857, 'orange'],
    [0.57142857142, 'orange'],
    [0.57142857142, 'gray'],
    [0.71428571428, 'gray'],
    [0.71428571428, 'yellow'],
    [0.85714285714,'yellow'],
    [0.85714285714,'pink'],
    [1,'pink']
]