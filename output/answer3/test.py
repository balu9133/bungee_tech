import pandas as pd
import numpy as np

veg = pd.read_csv("veg.csv")
veg.head()

sort = veg[['Team','Yellow Cards','Red Cards']]

v = sort.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
v

v.to_csv("main.csv")