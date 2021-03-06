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

# https://matplotlib.org/1.3.1/users/legend_guide.html
# reorder legend
flag_reorder = False
if flag_reorder:
  handles1, labels1 = plt.gca().get_legend_handles_labels()
  print("Original label order: ", labels1)
  order = [1, 0, 2]
  handles2, labels2 = ([handles1[idx] for idx in order], [labels1[idx] for idx in order])
  print("Adjusted label order: ", labels1)
  plt.legend(handles2, labels2, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
else:
  # Put the legend out of the figure
  plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()
print()


# histogram
sns.histplot(data=df_return_calc, x=Delta_x')
