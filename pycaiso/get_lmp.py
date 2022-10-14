from datetime import datetime

import pandas as pd

from pycaiso.oasis import Node

# select pnode

cj = Node("NCMETER_1_N001")

# create dataframe with LMPS from arbitrary period (30 day maximum). 

cj_lmps = cj.get_lmps(datetime(2021, 1, 1), datetime(2021, 1, 2))

print(cj_lmps.head())

cj_lmps.to_csv("NCMETER_1_N001.csv")