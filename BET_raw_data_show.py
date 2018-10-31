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

with open(input_name, 'r', errors = 'ignore') as f:      # 有亂碼，直接忽略檔案中的亂碼
    count = 0
    #BET_area = ' '
    for index, line in enumerate(f):
        count += 1
        if line[33 : 49] == 'BET Surface Area':
            BET_area = line[ 54: 60]

print(count)

test = '                                 BET Surface Area'
test[33:49]