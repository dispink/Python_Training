#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 15:18:46 2018

@author: DisPink
"""

'''https://medium.com/pyradise/
%E4%BD%BF%E7%94%A8-python-%E4%BE%86%E8%AA%8D%E8%AD%98%E5%90%91%E9%87%8F-5dda00162670'''

'Vectors'


import numpy as np

u = np.array([3, -1]).reshape(2,1)
v = np.array([8, 4, 0]).reshape(3,1)
w = np.array([-1, 0, 0, 3]).reshape(4, 1)
x = np.array([4, 0, -3, 2, 1]).reshape(5, 1)

print(u)
print(v)
print(w)
print(x)

'use .shape and .size to know the shpe and size'

vectors = [u, v, w, x]
for vec in vectors:
    print(vec.shape)
    print(vec.size)
    print("---")
