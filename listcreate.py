from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.sagan import DnsResult
from measurements import kwargs_a, kwargs_b, kwargs_c, kwargs_f, kwargs_g, kwargs_i, kwargs_x, kwargs_y, kwargs_z
import datetime
import numpy as np
from sklearn import preprocessing

# Function that parses the results for a measurement and puts the soaserial and timestamp in 2 lists and then returns
# those lists
def create_list(kwargs):
    is_success, results = AtlasResultsRequest(**kwargs).create()
    if is_success:
        l_soa = []
        l_time = []
        count = 0
        while count < len(results)-1:
            my_error = DnsResult(results[count])
            if not my_error.is_error:
                timestamp = results[count]['timestamp']
                #timestamp = datetime.datetime.fromtimestamp(timestamp)
                #timestamp = timestamp.strftime("%H:%M")
                soa_serial = results[count]['result']['answers'][0]['SERIAL']
                l_soa.append(soa_serial)
                l_time.append(timestamp)
            count += 1
        return l_soa, l_time


# Create a time list and soa list for each measurement
a = create_list(kwargs_a)
b = create_list(kwargs_b)
c = create_list(kwargs_c)
f = create_list(kwargs_f)
g = create_list(kwargs_g)
i = create_list(kwargs_i)
x = create_list(kwargs_x)
y = create_list(kwargs_y)
z = create_list(kwargs_z)

# Making a combined time/soa list for all servers
all_soa_list = [a[0], b[0], c[0], f[0], g[0], i[0], x[0], y[0], z[0]]
all_time_list = [a[1], b[1], c[1], f[1], g[1], i[1], x[1], y[1], z[1]]

# Setting colorbar tick values
for item in all_soa_list:
    unique = np.unique(item)

# Setting average datetime values
av = [float(sum(l)) / len(l) for l in zip(*all_time_list)]
timelist = []
for x in av:
    dt = datetime.datetime.fromtimestamp(x)
    timelist.append(dt)
