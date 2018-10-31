# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 18:01:36 2018

@author: Arthur
"""
import os

path = 'D:\\Google drive\\Acadamics\\Research\\Methods_BET\\raw'
os.chdir(path)
#file = input()

input_name = 'OR-S-B1.txt'
l_start = 0
pore_distribution = []
with open(input_name, 'r', errors = 'ignore') as f:      # 有亂碼，直接忽略檔案中的亂碼

    for index, line in enumerate(f):
        #if line[33 : 49] == 'BET Surface Area':
            #BET_area = line[ 54: 60]
        if line[0:32] == 'BJH Adsorption dV/dD Pore Volume':
            l_start = index  + 4
        if index >= l_start & index <= l_start + 26:
            pore_distribution.append(line)


test = 'BJH Adsorption dV/dD Pore Volume'
len(test)
test[33:49]