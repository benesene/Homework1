#!/usr/bin/env python3

import pandas as pd
import numpy as np

fly = pd.read_csv("flightdelay2007.csv")
numb=fly["Dest"].value_counts()
print(numb.head(3))






