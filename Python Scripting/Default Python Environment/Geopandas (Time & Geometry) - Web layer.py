import geopandas
from arcgis.features import GeoAccessor, GeoSeriesAccessor
import arcgis
import pandas as pd
import numpy as np
from datetime import datetime

url = r"" # URL for your ArcGIS Organization
username = "" # Your ArcGIS username
password = "" # Your ArcGIS password

gis = arcgis.gis.GIS(url, username, password)

flayer = gis.content.get('dede597f2fc54ae09b16508a0c70f62b').layers[0]

fset = flayer.query()
gjson = fset.to_geojson

for i in range(len(gdf['new_time'].array)):
    gdf['new_time'][i] = datetime.fromtimestamp(int(gdf['new_time'][i])/1000.0).strftime("%d-%B-%Y %H:%M:%S")

gdf_sub = gdf[['geometry', 'new_time', 'fid_']]

%insights_return(gdf_sub)