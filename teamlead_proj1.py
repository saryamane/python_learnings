#!/usr/bin/python

import pandas as pd

# fh = open('delivery_data.csv','r')
# counter = 0
# while counter < 10:
# 	for i in fh.readlines():
# 		counter = counter + 1
# 		print i

data = pd.read_csv("delivery_data.csv")

first = data.head(5)

print first