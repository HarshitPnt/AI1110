import numpy as np
import pandas as pd

df = pd.read_excel('raw.xlsx', 'Sheet1')
A = df.columns.to_numpy()
A_srt = np.sort(A)
df_srt = pd.DataFrame(A_srt)
df_srt = df_srt.transpose()
df_srt.to_excel('sort.xlsx', header=False, index=False)