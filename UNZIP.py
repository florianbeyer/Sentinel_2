# -*- coding: utf-8 -*-
"""
Batch process to unzip data.


MIT License Copyright (c) 2018 Florian Beyer
----------------------------------------------------------------------------


Script is unzipping all data in one folder.
Afterwards all zip-files are deleted
"""
#packages
from os import listdir, remove
from os.path import join
import numpy as np
import zipfile


# choose directory: where the zip files are saved?
load_path = "C:\\path\\to\\the\\data"



# start Process
allfiles = []
for fil in listdir(load_path):
    if fil.endswith(".zip"):
        allfiles.append(fil)
del (fil)

allNames = np.copy(allfiles)
for i in range(0,len(allfiles)):
    allNames[i] = allfiles[i][:-4]


for i in range(0,len(allfiles)):
    zipf = join(load_path, allfiles[i])
    
    zip_ref = zipfile.ZipFile(zipf, 'r')
    zip_ref.extractall(load_path)
    zip_ref.close()
    print 'ZIP file: {} extracted, {} / {}'.format(allNames[i], i+1, len(allNames))
    remove(zipf)
    print 'ZIP file:  {} removed'.format(allNames[i])
print 'Job done!'