# -*- coding: utf-8 -*-
"""
Downloading Sentinel2 data.

MIT License Copyright (c) 2018 Florian Beyer

----------------------------------------------------------------------------


Script is Downloading Sentinel 2a and 2b in Level2A

input parameters:
- start and end date
- boundary box as geojson file (see bellow)

more Information:

https://sentinelsat.readthedocs.io/en/stable/api.html#quickstart
https://scihub.copernicus.eu/twiki/do/view/SciHubUserGuide/3FullTextSearch
"""

# used python package
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt


# -------------------------------------------
# necessary information:
user = 'username'
password = 'password'

# YYYYMMDD
start_date = '20150101'
end_date = '20180207'

# map.geojson with boundary coordinates
# just generate and save as "map.geojson" using: --- http://geojson.io ---
geojson_path = 'directory\\to\\the\\file\\map.geojson'


# where to save the data
save_path = 'directory\\to\\the\\save_folder'


# -------------------------------------------

# connect to the API / SentinelHub
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus', show_progressbars=True)
footprint = geojson_to_wkt(read_geojson(geojson_path))
products = api.query(footprint,date=(start_date, end_date), platformname='Sentinel-2', producttype='S2MSI2Ap')
print 'Number of images: {}'.format(len(products))
api.download_all(products, save_path)

