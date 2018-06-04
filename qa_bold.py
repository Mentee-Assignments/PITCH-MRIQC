#!/usr/bin/env python
from glob import glob
import numpy as np
import pandas as pd
import os

# Step 1: find all *_bold.json files (os and glob) (result is a list)
# Step 2: iterate over all *_bold.json files
#   Step 2.1: check if fd_perc >= 50%
#   Step 2.2: store filename (*_bold.json) in a list.
# Step 3: write out list of files that matched the criteria