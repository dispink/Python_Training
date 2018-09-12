# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a, b = 0, 1
while a < 10:
    print(a, end = ",")
    a, b = b, a+b

words = ["cat", "window", "defenestrate"]

for w in words:
    print(w, len(w))

'-----------Application of numpy----------'
'''https://medium.com/pyradise/%E8%AA%8D%E8%AD%98-python-
%E7%A7%91%E5%AD%B8%E9%81%8B%E7%AE%97%E5%A5%97%E4%BB%B6-c4e59f1d8ecc'''

import numpy as np
dist_in_km = list(range(3,10))
dist_in_km = np.array(dist_in_km)
dist_in_mile = dist_in_km * 0.62137
print(dist_in_mile)

import numpy as np

dist_in_km = list(range(3,10))
print(type(dist_in_km))
dist_in_km = np.array(dist_in_km)
print(type(dist_in_km))

lst = [42.95, 'km', True]
for i in lst:
    print(type(i))

# use .reshape to construct different dimensions of ndarray
#0 Dimension: scalar

my_scalar = 87
print(my_scalar)


#1 Divmension: vector
#a column of scalar assembly

import numpy as np

arr = np.array(lst)
for i in arr:
    print(type(i))
    
u = np.array([8, 7]).reshape(2, 1)
v = np.array([8, 7, 6]).reshape(3,1)

print(u)
print("\n")
print(v)


#2 Dimension: matrix#
#columns and rows of scalar assembly

import numpy as np

my_mat = np.arange(1, 13).reshape(4,3)
print(my_mat)

'tensor'

import numpy as np

my_tensor = np.arange(1, 25).reshape(2, 4, 3)   #(2, 4, 3) means two 4X3 matrice
print(my_tensor)




