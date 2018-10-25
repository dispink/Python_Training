# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:17:58 2018
Take core NKE-1 as target to re-show my mater thesis using R
input data: 
pair data: 
"""

import pandas as pd
import numpy as np
from scipy import stats
import seaborn

# input source excel            
df_data = (pd.read_excel('Results_NK-1-W_3rd_20151008.xls', 'Results_NK-1-W_3rd_20151008', skiprows = 2).
           rename(columns = {"position (mm)" : "position_mm"}).
           dropna()
           )
df_data.head()

# input master result
df_pair = pd.read_csv('NKE-1_clr_cor_compile_0430.csv')
df_pair.head()


# select the elements and position columns

df_data_sel = df_data.loc[ : , ['Si', 'K', 'Ca', 'Ti', 'Cr', 'Br', 'Mn', 'Fe', 'Ni',
                                'Cu', 'Zn', 'Pb', 'Zr', 'Rb', 'Mo coh']].copy()
position = df_data['position_mm']
## replace zero to avoid problems with transform
#  replace the 0 value with the mean of first 25% observation values in Br & Pb.
df_data_sel.describe().min()    #only Br and Pb has 0

df_data_sel.Br = df_data_sel.Br.replace( 
        0, df_data_sel.describe().loc['25%', 'Br']
        )

df_data_sel.Pb = df_data_sel.Pb.replace( 
        0, df_data_sel.describe().loc['25%', 'Pb']
        )

df_data_sel.describe().min()
# maybe later can use randomnormal number between 1 and 0.1% (-3std) to replace 0
 
# centred log-ratio
df_clr = pd.DataFrame()
gm = stats.gmean(df_data_sel, axis = 1)
for nrow in range(len(df_data_sel)):
    df_clr = df_clr.append(
            np.log(df_data_sel.iloc[nrow]/gm[nrow])
            )

# why the order of columns is re-sorted....???
    # so I need to manually re-order the columns...
df_clr = df_clr[['Si', 'K', 'Ca', 'Ti', 'Cr', 'Br', 'Mn', 'Fe', 'Ni',
                                'Cu', 'Zn', 'Pb', 'Zr', 'Rb', 'Mo coh']]

# eveluate the difference compare to the master result (take Si as representative)
diff_Si = df_clr['Si'] - df_pair['Si']
diff_Si.plot('hist')        # they are almost identical

sns_plot = seaborn.pairplot(df_clr)
sns_plot.savefig('NKE-1_pairs.png')        # it's almost identical to the master result

# PCA
