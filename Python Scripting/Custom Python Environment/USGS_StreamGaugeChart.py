# first import the functions for downloading data from NWIS
import dataretrieval.nwis as nwis
import pandas as pd
import matplotlib as plt

# specify the USGS site code for which we want data.
site = '02146670'
df = nwis.get_record(sites=site, service='dv', start='2020-01-01', end='2021-12-31', parameterCd='00060')
df['00060_Mean'].plot(linewidth=0.5)
plt.pyplot.show()

#Convert time to string for Insights ease of use
df = df.reset_index()
df['datetime'] = df['datetime'].astype(str).str[0:10]
df.head(5)
type(df['datetime'][0])
%insights_return(df)

