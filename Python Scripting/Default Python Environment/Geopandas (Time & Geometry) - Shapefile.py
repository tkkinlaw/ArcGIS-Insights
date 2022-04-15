import geopandas

shapeFilePath = r"" # You shapefile file path here <--

shp = geopandas.read_file(shapeFilePath)

shp['new_time'] = shp['new_time'].astype(str)

shp_sub = shp[['geometry', 'shift', 'fid_', 'new_time']] # List your fields of interest

shp_sub.head(5)

%insights_return(shp_sub)