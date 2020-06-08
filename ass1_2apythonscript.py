#!/usr/bin/env python3

import pandas as pd
import numpy as np

fly = pd.read_csv("flightdelay2007.csv")
high = fly[fly["Origin"]=="SFO"]["ArrDelay"] 
rowdata = high.head(3)
col_headers = ['ArrDelay']
final = pd.DataFrame(rowdata,columns=col_headers)

print(final)











