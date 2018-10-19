# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:17:58 2018

Take core NKE-1 as target to re-show my mater thesis using R
"""

import pandas as pd
import numpy as np
from scipy import stats

# input source excel 
input_file = "D:/Google drive/Acadamics/Research/Methods_ITRAX/EPA_project_2015/NK-1_W_20151008_3rd/NK-1-W_3rd_xrf_1mm_0-940mm_30kv26ma15sr1/Results_NK-1-W_3rd_20151008.xls"
df_data = (pd.read_excel(input_file, "Results_NK-1-W_3rd_20151008", skiprows = 2).
           rename(columns = {"position (mm)" : "position_mm"}).
           dropna()
           )
df_data.head()

# input master result
df_pair = pd.read_csv('D:/Google drive/Acadamics/Research/Methods_Statistics/2017-04/compile_final_0430/NKE-1_clr_cor_compile_0430.csv')
df_pair.head()


# select the elements and position columns

df_data_sel = df_data.loc[ : , ['Si', 'K', 'Ca', 'Ti', 'Cr', 'Br', 'Mn', 'Fe', 'Ni',
                                'Cu', 'Zn', 'Pb', 'Zr', 'Rb', 'Mo coh']].copy()
position = df_data['position_mm']
# replace 0 by 1 since 0 will cause the infinite problem in letter centred log-ratio transformation.
# 0 reflect the concentration meet the detect limit of Itrax, so use 1 can represent the low count as well and avoid the problem.
df_data_sel = df_data_sel.replace(0,1)
df_data_sel.describe().min()

# centred log-ratio
df_clr = pd.DataFrame()
gm = stats.gmean(df_data_sel, axis = 1)
for nrow in range(0, len(df_data_sel)):
    df_clr = df_clr.append(
            np.log(df_data_sel.iloc[nrow]/gm[nrow])
            )
# why the order of columns is sorted....???
    
df_clr['position_mm'] = position
df_clr['Si'].head()   
df_pair['Si'].head() 

round(df_clr['Si'] - df_pair['Si'], 3)
print(df_clr.loc[1, 'Si'], '\n', df_pair.loc[1, 'Si'])
# some differences should be made by the 0 replacement difference between the Master thesis and here.