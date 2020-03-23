import pandas as pd
import numpy as np
from listcreate import a, b, c, f, g, i, x, y, z
import datetime

unique = np.unique(a[0])


def merge(list1, list2):
    merged_list = [(list1[s], list2[s]) for s in range(0, len(list1))]
    return merged_list

# Make tuples for the lists
tuple_a=merge(a[0], a[2])
tuple_b=merge(b[0], b[2])
tuple_c=merge(c[0], c[2])
tuple_f=merge(f[0], f[2])
tuple_g=merge(g[0], g[2])
tuple_i=merge(i[0], i[2])
tuple_x=merge(x[0], x[2])
tuple_y=merge(y[0], y[2])
tuple_z=merge(z[0], z[2])


def filter_value(someList, value):
    for d, e in someList:
        if d == value :
            yield d,e

# Filter out the soa values
a_=[]
for count in unique:
    result=list(filter_value(tuple_a, count))
    a_.append(result)

b_=[]
for count in unique:
    result=list(filter_value(tuple_b, count))
    b_.append(result)

c_=[]
for count in unique:
    result=list(filter_value(tuple_c, count))
    c_.append(result)

f_=[]
for count in unique:
    result=list(filter_value(tuple_f, count))
    f_.append(result)

g_=[]
for count in unique:
    result=list(filter_value(tuple_g, count))
    g_.append(result)

i_=[]
for count in unique:
    result=list(filter_value(tuple_i, count))
    i_.append(result)

x_=[]
for count in unique:
    result=list(filter_value(tuple_x, count))
    x_.append(result)

y_=[]
for count in unique:
    result=list(filter_value(tuple_y, count))
    y_.append(result)

z_=[]
for count in unique:
    result=list(filter_value(tuple_z, count))
    z_.append(result)

def unique_list(list):
    k=0
    ul =[]
    while k < len(list):
        un_result = list[k][0]
        ul.append(un_result)
        k += 1
    return ul

# Create list for the unique values
al=unique_list(a_)
bl=unique_list(b_)
cl=unique_list(c_)
fl=unique_list(f_)
gl=unique_list(g_)
il=unique_list(i_)
xl=unique_list(x_)
yl=unique_list(y_)
zl=unique_list(z_)

all_tuple_list=[al, bl, cl, fl, gl, il, xl, yl, zl]
# Create dataframe
a_df= pd.DataFrame(al, columns=['soa', 'timestamp'])
b_df= pd.DataFrame(bl, columns=['soa', 'timestamp'])
c_df= pd.DataFrame(cl, columns=['soa', 'timestamp'])
f_df= pd.DataFrame(fl, columns=['soa', 'timestamp'])
g_df= pd.DataFrame(gl, columns=['soa', 'timestamp'])
i_df= pd.DataFrame(il, columns=['soa', 'timestamp'])
x_df= pd.DataFrame(xl, columns=['soa', 'timestamp'])
y_df= pd.DataFrame(yl, columns=['soa', 'timestamp'])
z_df= pd.DataFrame(zl, columns=['soa', 'timestamp'])

# Create dict
a_dict=a_df.to_dict()
b_dict=b_df.to_dict()
c_dict=c_df.to_dict()
f_dict=f_df.to_dict()
g_dict=g_df.to_dict()
i_dict=i_df.to_dict()
x_dict=x_df.to_dict()
y_dict=y_df.to_dict()
z_dict=z_df.to_dict()

# make lists
asoa=[a_df['soa'].to_list(), ['a.ns.se']]
atime=a_df['timestamp'].to_list()
bsoa=[b_df['soa'].to_list(),['b.ns.se']]
btime=b_df['timestamp'].to_list()
csoa=[c_df['soa'].to_list(), ['c.ns.se']]
ctime=c_df['timestamp'].to_list()
fsoa=[f_df['soa'].to_list(), ['f.ns.se']]
ftime=f_df['timestamp'].to_list()
gsoa=[g_df['soa'].to_list(), ['g.ns.se']]
gtime=g_df['timestamp'].to_list()
isoa=[i_df['soa'].to_list(), ['i.ns.se']]
itime=i_df['timestamp'].to_list()
xsoa=[x_df['soa'].to_list(), ['x.ns.se']]
xtime=x_df['timestamp'].to_list()
ysoa=[y_df['soa'].to_list(), ['y.ns.se']]
ytime=y_df['timestamp'].to_list()
zsoa=[z_df['soa'].to_list(), ['z.ns.se']]
ztime=z_df['timestamp'].to_list()

# Combined time and soa lists
some_soa_list =[asoa, bsoa, csoa, fsoa, gsoa, isoa, xsoa, ysoa, zsoa]
some_time_list =[atime, btime, ctime, ftime, gtime, itime, xtime, ytime, ztime]

# Colorbar ticks

'''for s in some_time_list:
    s.sort()
av = [float(sum(l)) / len(l) for l in zip(*some_time_list)]
colorticks = []
for count in av:
    dt = datetime.datetime.fromtimestamp(count)
    colorticks.append(dt)
'''
