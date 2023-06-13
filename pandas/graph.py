
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pandas/ds_salaries.csv')

df.plot()
# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# df["Duration"].plot(kind = 'hist')

# plt.savefig('plot3.png')

plt.show()
#Two  lines to make our compiler able to draw:
