#!/usr/bin/env python
from glob import glob
import numpy as np
import pandas as pd
import os
import json
import csv

# Step 1: find all *_bold.json files (os and glob) (result is a list)
path = os.path.join(os.getcwd(), "derivatives", "*_bold.json")
f_list = glob(path)

# Step 2: iterate over all *_bold.json files
perc_greater_than_50 = []
for files in f_list:
    with open(files) as f:
        objects = json.load(f)
        if objects['fd_perc'] >= 50: #   Step 2.1: check if fd_perc >= 50%
            perc_greater_than_50.append(files)#   Step 2.2: store filename (*_bold.json) in a list.

# Step 3: write out list of files that matched the criteria
with open('fd_prec.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(perc_greater_than_50)
    
