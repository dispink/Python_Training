#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 09:54:40 2018

@author: DisPink
"""

'plot vector in a plane'

import matplotlib.pyplot as plt
import seaborn
seaborn.reset_orig()
    
def plot_a_vector(x, y, tick=2):
  """
  描繪一個 (x, y) 的向量
  """
  # 向量的起始點
  x0 = 0
  y0 = 0
  # 指定向量的終點
  dx = x
  dy = y
  # 指定座標軸的範圍
  max_val = max(abs(dx), abs(dy)) + 2
  plt.xlim(-max_val, max_val)
  plt.ylim(-max_val, max_val)
  ax = plt.gca()
  # 外框隱藏掉兩邊
  ax.spines['top'].set_color('none')
  ax.spines['right'].set_color('none')
  # 將剩餘的兩邊外框挪到原點
  ax.xaxis.set_ticks_position('bottom')
  ax.spines['bottom'].set_position(('data',0))
  ax.yaxis.set_ticks_position('left')
  ax.spines['left'].set_position(('data',0))
  # 標註文字
  if dx >= 0:
    adjust = 0.5
  else:
    adjust = -3
  ax.annotate('({}, {})'.format(dx, dy), xy=(dx, dy), xytext=(dx + adjust, dy))
  # 畫出向量
  plt.arrow(x0, y0, dx, dy, length_includes_head=True, head_width=0.3)
  # 調整刻度標籤
  plt.xticks(range(-max_val + 1, max_val - 1, tick))
  plt.yticks(range(-max_val + 1, max_val - 1, tick))


plt.subplot(2, 2, 1)
plot_a_vector(1, 4)

plt.subplot(2, 2, 2)
plot_a_vector(-5, 3)

plt.subplot(2, 2, 3)
plot_a_vector(-1, -5)

plt.subplot(2, 2, 4)
plot_a_vector(2, -3)
