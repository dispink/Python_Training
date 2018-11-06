# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 14:13:35 2018

@author: Arthur
"""

import os
from os import listdir
import platform
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

"""
color in plot can use the strings below to define:
1.one of {'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 
'tab:gray', 'tab:olive', 'tab:cyan'} which are the Tableau Colors from the 'T10' 
categorical palette (which is the default color cycle);

2.one of {'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'} --> this follow the style you set
"""

# set workinf directory
if platform.system() == 'Darwin':
    path = '/Users/DisPink/Google Drive/Acadamics/Research/Methods_FTIR/raw'
if platform.system() == 'Windows':
    path = 'D:\\Google drive\\Acadamics\\Research\\Methods_FTIR\\raw'
os.chdir(path)

def FTIR_convector(input_file):
    wv_list = []
    int_list = []
    sample_ID = []
    with open(input_file, 'r') as f:
        for line in f:
            wv, intensity = line.split()
            wv_list.append(float(wv))
            int_list.append(float(intensity))
            sample_ID.append(input_file[9:-4])
        d ={'wavenumber': wv_list,
            'intensity': int_list,
            'sample_ID': sample_ID}
        ftir = pd.DataFrame(data = d)
    return ftir
        
        
ftir_df = pd.DataFrame()
for file in listdir():
    if file[-3:] == 'PRN':
        ftir_df = ftir_df.append(
                FTIR_convector(file)
                )

### plot using matplotlib.pyplot.subplots
fig, ax = plt.subplots(2, 1, figsize=(9, 8)) 
ax[1].plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-B3']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-B3']['intensity'],
         label = 'After sieving',
         color = 'C1', alpha = 0.5, linewidth = 1
         )

ax[1].plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-BC1']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-BC1']['intensity']+2,
         label = 'After sieving, removing IC',
         color = 'C2', alpha = 0.5, linewidth = 1
         )

ax[1].plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-BCH2']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-BCH2']['intensity']+4,
         label = 'After sieving, removing IC, removing OC (NaOCl)',
         color = 'C4', alpha = 0.5, linewidth = 1
         )
ax[1].text(3000, 2, 'After sieving')
ax[1].text(3500, 4, 'After sieving, removing IC')
ax[1].text(3500, 6.2, 'After sieving, removing IC, removing OC (NaOCl)')
ax[1].set_ylim(1, 7.5)
ax[1].set_xlim(4100, 250)
ax[1].get_yaxis().set_ticks([])    # make y-axis invisible, but can still plot labels
ax[1].set_xlabel('wavenumber ({})'.format(r'$cm^{-1}$'))
ax[1].set_ylabel('intensity')

### plot overlaping spectrum using matplotlib.pyplot.subplots
ax[0].plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-B3']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-B3']['intensity'],
         label = 'After sieving',
         color = 'C1', alpha = 0.5, linewidth = 1
         )

ax[0].plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-BC1']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-BC1']['intensity'],
         label = 'After sieving, removing IC',
         color = 'C2', alpha = 0.5, linewidth = 1
         )

ax[0].plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-BCH2']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-BCH2']['intensity'],
         label = 'After sieving, removing IC, removing OC (NaOCl)',
         color = 'C4', alpha = 0.5, linewidth = 1
         )

ax[0].set_ylim(1, 4)
ax[0].set_xlim(4100, 250)
ax[0].set_title('FTIR adsorption spectrum')
ax[0].set_xlabel('wavenumber ({})'.format(r'$cm^{-1}$'))
ax[0].set_ylabel('intensity')
ax[0].legend()

fig.savefig('{}FTIR_result_20181101.pdf'.format(path[:-3]), bbox_inches = 'tight')  





### plot using matplotlib.pyplot only
plt.figure(figsize=(9,4))
plt.plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-B3']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-B3']['intensity'],
         label = 'After sieving',
         color = 'C1', alpha = 0.5, linewidth = 1
         )

plt.plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-BC1']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-BC1']['intensity']+2,
         label = 'After sieving, removing IC',
         color = 'C2', alpha = 0.5, linewidth = 1
         )

plt.plot(ftir_df[ftir_df['sample_ID'] == 'OR-S-BCH2']['wavenumber'],
         ftir_df[ftir_df['sample_ID'] == 'OR-S-BCH2']['intensity']+4,
         label = 'After sieving, removing IC, removing OC (NaOCl)',
         color = 'C4', alpha = 0.5, linewidth = 1
         )
plt.text(3000, 2, 'After sieving')
plt.text(3500, 4, 'After sieving, removing IC')
plt.text(3500, 6.2, 'After sieving, removing IC, removing OC (NaOCl)')
plt.ylim(1, 7.5)
plt.xlim(4100, 250)
plt.yticks([])      # make y-axis invisible, but can still plot labels
plt.xlabel('wavenumber ({})'.format(r'$cm^{-1}$'))
plt.ylabel('intensity')
plt.title('FTIR adsorption spectrum')

plt.savefig('{}FTIR_result_20181101.pdf'.format(path[:-3]), bbox_inches = 'tight')  

print('''here I practice two plotting code which produce same figure.
      however, the subplots method will be useful when plotting multiple axes in a figure.''')

