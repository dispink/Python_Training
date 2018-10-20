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
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

## input source excel ##           
data_df = (pd.read_excel('Results_NK-1-W_3rd_20151008.xls', 'Results_NK-1-W_3rd_20151008', skiprows = 2).
           rename(columns = {"position (mm)" : "position_mm"}).
           dropna()
           )
data_df.head()

# input master result #
pair_df = pd.read_csv('NKE-1_clr_cor_compile_0430.csv')
pair_df.head()


# select the elements and position columns

data_sel_df = data_df.loc[ : , ['Si', 'K', 'Ca', 'Ti', 'Cr', 'Br', 'Mn', 'Fe', 'Ni',
                                'Cu', 'Zn', 'Pb', 'Zr', 'Rb', 'Mo coh']].copy()
position = data_df['position_mm']

# replace zero to avoid problems with transform
#  replace the 0 value with the mean of first 25% observation values in Br & Pb.
data_sel_df.describe().min()    #only Br and Pb has 0

data_sel_df.Br = data_sel_df.Br.replace( 
        0, data_sel_df.describe().loc['25%', 'Br']
        )

data_sel_df.Pb = data_sel_df.Pb.replace( 
        0, data_sel_df.describe().loc['25%', 'Pb']
        )

data_sel_df.describe().min()
# maybe later can use randomnormal number between 1 and 0.1% (-3std) to replace 0
 
## centred log-ratio ##
clr_df = pd.DataFrame()
gm = stats.gmean(data_sel_df, axis = 1)
for nrow in range(len(data_sel_df)):
    clr_df = clr_df.append(
            np.log(data_sel_df.iloc[nrow]/gm[nrow])
            )

# why the order of columns is re-sorted....???
    # so I need to manually re-order the columns...
clr_df = clr_df[['Si', 'K', 'Ca', 'Ti', 'Cr', 'Br', 'Mn', 'Fe', 'Ni',
                                'Cu', 'Zn', 'Pb', 'Zr', 'Rb', 'Mo coh']]

# eveluate the difference compare to the master result (take Si as representative)
diff_Si = clr_df['Si'] - pair_df['Si']
diff_Si.plot('hist')        # they are almost identical

sns_plot = seaborn.pairplot(clr_df)
sns_plot.savefig('NKE-1_pairs.png')        # it's almost identical to the master result

## PCA ##
x = StandardScaler().fit_transform(clr_df)   # need to standardized first

pca = PCA(n_components = 'mle', svd_solver = 'full')         # let's try the fancy automatically selection
PCs = pca.fit_transform(x)
PCs_df = pd.DataFrame(data = PCs) 
variance = pca.explained_variance_ratio_
    
print('automatically select {} components. \n {}% of variance is retianed.'.format(
        len(variance), round(variance.sum()*100) )
    ) 
print('the auto selection is a shit.... only exclude one component... need to dig more about it..')

pca = PCA( n_components = 3)        # based on my master result
PCs = pca.fit_transform(x)
PCs_df = pd.DataFrame(
        data = PCs,
        columns = ['PC1', 'PC2', 'PC3'])


