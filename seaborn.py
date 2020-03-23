import numpy as np
import datetime
from parser import a_df
import seaborn as sns
import matplotlib.pyplot as plt

df = a_df.pivot("soa", "timestamp")
f,(ax1,ax2,ax3) = plt.subplots(3, 1, sharex='all')
g1 = sns.heatmap(df, cmap="PiYG",cbar=False,ax=ax1)
g1.set_ylabel('')
g1.set_xlabel('')
g2 = sns.heatmap(df, cmap="PiYG",cbar=False,ax=ax2)
g2.set_ylabel('')
g2.set_xlabel('')
g3 = sns.heatmap(df, cmap="PiYG",ax=ax3)
g3.set_ylabel('')
g3.set_xlabel('')
plt.show()