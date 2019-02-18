import numpy as np;
import pandas as pd;
from pandas import DataFrame, Series

records=[line for line in open("../data/m.json")]
f=DataFrame(records)

print(f)

fz=f[u'name'].value_counts()

# print(fz[:10])

# fz_counts[:10].plot(kind='barh',rot=0)
