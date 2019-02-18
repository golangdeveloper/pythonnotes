from pandas import DataFrame,Series

import pandas as pd;
import numpy as np;

records=[line for line in open("../data/m.json")]
f=DataFrame(records)

print(f)

fz=f[u'name'].value_counts()

# print(fz[:10])

# fz_counts[:10].plot(kind='barh',rot=0)
