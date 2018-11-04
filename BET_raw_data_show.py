# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:01:36 2018

@author: Arthur
"""
import os
from os import listdir
import platform
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns

# set workinf directory
if platform.system() == 'Darwin':
    path = '/Users/DisPink/Google Drive/Acadamics/Research/Methods_BET/raw'
if platform.system() == 'Windows':
    path = 'D:\\Google drive\\Acadamics\\Research\\Methods_BET\\raw'
os.chdir(path)


def convert_raw(input_name):
    
    l_start = 0
    pore_distribution = []
    with open(input_name, 'r', errors = 'ignore') as f:      # 有亂碼，直接忽略檔案中的亂碼

        for index, line in enumerate(f):
            if line[33 : 49] == 'BET Surface Area':
                BET_area = line[ 54: 60]
            if line[0:32] == 'BJH Adsorption dV/dD Pore Volume':
                l_start = index  + 5
    

    with open(input_name, 'r', errors = 'ignore') as f:
        for index, line in enumerate(f):
            if (index >= l_start) and (index <= l_start + 24):
                #print(line.split('\t'))
                pore_distribution.append(line.split('\t'))
             
                pore_df = pd.DataFrame(pore_distribution, columns = ['pore_diameter', 'pore_volume'])

    for line in range(len(pore_df)):
        pore_df.iloc[line, 0] = float(pore_df.iloc[line, 0][:6])
        pore_df.iloc[line, 1] = float(pore_df.iloc[line, 1][:13])
        pore_df['sample_ID'] = input_name[:-4]
        pore_df['BET_area'] = BET_area
    
    return pore_df


pore_df = pd.DataFrame()
for i in range( len(listdir()) ):
    if listdir()[i][-3:] == 'TXT':
        pore_df = pore_df.append(
                convert_raw(listdir()[i])
                )
# set tyoe for later plotting        
pore_df['pore_diameter'] = pore_df['pore_diameter'].astype(float)
pore_df['pore_volume'] = pore_df['pore_volume'].astype(float)
pore_df['BET_area'] = pore_df['BET_area'].astype(float)      

## plotting

# use seaborn #
ax = sns.lineplot(x = 'pore_diameter',
                  y = 'pore_volume',
                  data = pore_df, 
                  hue = 'sample_ID',
                  alpha = 0.5)
ax.set(xlabel = 'pore diameter (nm)', 
       ylabel = 'pore volume ({})'.format(r'$cm^3 / g \cdot nm $'))
ax.set_xlim(0, 20)
ax.figure()
ax.figure.savefig('pore distribution sns.pdf')

# use matplotlib #
# plot the untreated samples
plt.scatter(
            pore_df[pore_df['sample_ID'] == 'OR-S-B1']['pore_diameter'],
            pore_df[pore_df['sample_ID'] == 'OR-S-B1']['pore_volume'],
            color = 'grey', s = 2, marker = 'o', 
            label = 'OR-S-B1, {} {}'.format(
                    pore_df[pore_df['sample_ID'] == 'OR-S-B1'].iloc[1,3],
                    r'$m^2 / g$')
            )
plt.scatter(
            pore_df[pore_df['sample_ID'] == 'OR-S-B2']['pore_diameter'],
            pore_df[pore_df['sample_ID'] == 'OR-S-B2']['pore_volume'],
            color = 'grey', s = 2, marker = '^', 
            label = 'OR-S-B2, {} {}'.format(
                    pore_df[pore_df['sample_ID'] == 'OR-S-B2'].iloc[1,3],
                    r'$m^2 / g$')
            )
plt.scatter(
            pore_df[pore_df['sample_ID'] == 'OR-S-B3']['pore_diameter'],
            pore_df[pore_df['sample_ID'] == 'OR-S-B3']['pore_volume'],
            color = 'grey', s = 2, marker = 's', 
            label = 'OR-S-B3, {} {}'.format(
                    pore_df[pore_df['sample_ID'] == 'OR-S-B3'].iloc[1,3],
                    r'$m^2 / g$')
            )

# plot the samples which IC are removed
plt.scatter(
            pore_df[pore_df['sample_ID'] == 'OR-S-BC1']['pore_diameter'],
            pore_df[pore_df['sample_ID'] == 'OR-S-BC1']['pore_volume'],
            color = 'dodgerblue', s = 2, marker = 'o', 
            label = 'OR-S-BC1, {} {}'.format(
                    pore_df[pore_df['sample_ID'] == 'OR-S-BC1'].iloc[1,3],
                    r'$m^2 / g$')
            )
plt.scatter(
            pore_df[pore_df['sample_ID'] == 'OR-S-BC2']['pore_diameter'],
            pore_df[pore_df['sample_ID'] == 'OR-S-BC2']['pore_volume'],
            color = 'dodgerblue', s = 2, marker = '^', 
            label = 'OR-S-BC2, {} {}'.format(
                    pore_df[pore_df['sample_ID'] == 'OR-S-BC2'].iloc[1,3],
                    r'$m^2 / g$')
            )
            
# plot the samples which OC are removed
plt.scatter(
            pore_df[pore_df['sample_ID'] == 'OR-S-BCH1']['pore_diameter'],
            pore_df[pore_df['sample_ID'] == 'OR-S-BCH1']['pore_volume'],
            color = 'firebrick', s = 2, marker = 'o', 
            label = 'OR-S-BCH1, {} {}'.format(
                    pore_df[pore_df['sample_ID'] == 'OR-S-BCH1'].iloc[1,3],
                    r'$m^2 / g$')
            )
plt.scatter(
            pore_df[pore_df['sample_ID'] == 'OR-S-BCH2']['pore_diameter'],
            pore_df[pore_df['sample_ID'] == 'OR-S-BCH2']['pore_volume'],
            color = 'firebrick', s = 2, marker = '^', 
            label = 'OR-S-BCH2, {} {}'.format(
                    pore_df[pore_df['sample_ID'] == 'OR-S-BCH2'].iloc[1,3],
                    r'$m^2 / g$')
            )
# settings of the plot
plt.title('Pore size distribution')
plt.xlim(0, 35)
plt.ylim(0, 0.006)
plt.xlabel('Pore diameter (nm)')
plt.ylabel('Pore volume ({})'.format(r'$cm^3 / g \cdot nm$'))
plt.legend(loc='upper right')
plt.savefig('{}pore_distribution_mat.pdf'.format(path[:-3]))
