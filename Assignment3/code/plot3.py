#code to sort excel sheet and print a plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('raw.xlsx', 'Sheet1')
A = df.columns.to_numpy()
A_srt = np.sort(A)
Y=[1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5,1.5]
plt.figure(figsize=(8, 2))
ax = plt.subplot(8, 1, 6)
plt.xlabel("Height (in cm)")
ax = plt.gca()
ax.tick_params(which='major', width=1.00)
ax.tick_params(which='major', length=10)
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=1.05)
plt.xticks(range(140,166))
plt.yticks([])
ax.axes.yaxis.set_visible(False)
ax.set_xlim(140, 165)
ax.set_ylim(0, 10)
ax.set_xticks(ax.get_xticks()[::2])
ax.scatter(A_srt,Y,alpha=0.9,c='blue',edgecolors='none',s=30)
ax.scatter([149],[1.5],alpha=0.9,c='red',edgecolors='none',s=30)
plt.show()

df_srt = pd.DataFrame(A_srt)
df_srt = df_srt.transpose()
df_srt.to_excel('sort.xlsx', header=False, index=False)