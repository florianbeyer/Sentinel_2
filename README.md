# Sentinel_2
Some scripts to download, unzip and process multiple Sentinel-2 datasets at once

1. DOWNLOADING Sentinel 2 data in Level2a (Reflectance Bottom of Atmopsphere)
DownloadS2.py + map.geojson (example json file)

2. unzip all downloaded data
UNZIP.py

3. processing data -pending-
the skript will process all downloaded datasets:
- choose 10m GSD
- subset a region of interest
- check cloud coverage
- if cloud free export as tiff
