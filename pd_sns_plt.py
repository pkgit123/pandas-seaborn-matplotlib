import pandas as pd
import numpy as np

pd.set_option("display.max_columns", 999)

%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

print('Seaborn version: ', sns.__version__)

# %%time

x='Delta_x'
y='Vega_x'
hue='Expiration_x'

sns.scatterplot(data=df_return_calc.head(50), x=x, y=y, hue=hue)

# put a title
plt.title(f"`{x}` vs. `{y}` with hue of `{hue}`")

# Rotates X-Axis Ticks by 90-degrees
plt.xticks(rotation = 90) 

# Put the legend out of the figure
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()
print()
