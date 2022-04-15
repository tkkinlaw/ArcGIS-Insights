import geopandas
import pandas as pd
from arcgis.features import GeoAccessor, GeoSeriesAccessor

fc = r"" # Your file path here <--

sdf = pd.DataFrame.spatial.from_featureclass(fc)

sdf['new_time'] = sdf['new_time'].astype(str)

featureset = sdf.spatial.to_featureset()
gjson = featureset.to_geojson
gdf = geopandas.read_file(gjson)

gdf_sub = gdf[['fid', 'geometry', 'new_time']] # List your fields of interest

%insights_return(gdf_sub)