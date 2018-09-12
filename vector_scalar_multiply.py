#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:55:06 2018

@author: DisPink
"""

import numpy as np
#向量與純量相乘
arr = np.array([2, 4]).reshape(2,1)
print(arr)
print('---')
print(3 * arr)
print('---')
print((0.5 * arr).astype(int))
print(0.5 * arr)
print('---')
print(-1 * arr)

#描繪向量與純量相乘
import matplotlib.pyplot as plt

plt.figure(figsize = (16, 4))
plt.subplot(1, 4, 1)
plot_a_vector(2, 4)
plt.subplot(1, 4, 2)
plot_a_vector(6, 12, 3)
plt.subplot(1, 4, 3)
plot_a_vector(1, 2, 1)
plt.subplot(1, 4, 4)
plot_a_vector(-2, -4)