#input_name = input()					#是讀取已經covert成csv檔的檔案
import os
import numpy as np
import matplotlib.pyplot as plt

input_file = os.path.expanduser('~/Documents/Python_Training/out.csv')	#python並不會自動展開~/的路徑，所以需要這個指令來展開
with open(input_file, 'r') as f:		#with...as...建立一個區塊中的某指令簡寫，當程式碼離開這個區塊(以對線做區隔)，便自動取消著個指令動作 
	data = []							#故也可做為自動close檔案的一個好方法
	for index, line in enumerate(f):
		if index == 0:
			column_info = line[:-1].split(',')       #enumerate讀入檔案會在最後加上\n，所以須拍除這一項
		else:
			data = data + [line[:-1].split(',')]

for index, value in enumerate(column_info):
    if value == 'Ar':
        ar_col = index
    if value == 'Fe':
        fe_col = index
    if value == 'MSE':
        mse_col = index
    if value == 'validity':
        vld_col = index
    if value == 'position (mm)':
        pos_col = index

ratio = []
mse = []
position_mm = []
for datum in data:
    ratio.append(float(datum[ar_col]) / float(datum[fe_col]))	#逐列加入Fe/Ar的比值於ratio中
    mse.append(float(datum[mse_col]))
    position_mm.append(int(datum[pos_col]))
# identify which points the Ar/Fe value is too high. this may indicate the points are cracks in core.
# leave the points that Ar/Fe value within 2 std of the total Fr/Fe & MSE within 1 std of the total MSE

ratio_std = np.std(ratio)
ratio_mean = np.mean(ratio)
mse_std = np.std(mse)
mse_mean = np.mean(mse)

ratio_1 = []
ratio_2 = []
pos_1 = []
pos_2 = []

for datum in data:
    cur_ratio = float(datum[ar_col])/float(datum[fe_col])
# selection strategy 1: ratio_1
# include the Ar/Fe value from 0 to mean + 1 std (83.85% population if normal distributed)
# include the MSE value from 0 to mean + 1 std (83.85% population if normal distributed)
# the validity must equal to 1
    if cur_ratio <= (ratio_std + ratio_mean) and float(datum[mse_col]) <= (mse_std + mse_mean) and datum[vld_col] == '1':       
            ratio_1.append(float(cur_ratio))
            pos_1.append(int(datum[pos_col]))

# selection strategy 2: ratio_2
# include the Ar/Fe value from 0 to mean + 1 std (83.85% population if normal distributed)
# include the MSE value smaller than 1.5 (practicle experience)
# the validity must equal to 1
    if cur_ratio <= (ratio_std + ratio_mean) and float(datum[mse_col]) <= 1.5 and datum[vld_col] == '1':
            ratio_2.append(float(cur_ratio))
            pos_2.append(int(datum[pos_col]))

#plot the Ar/Fe scatterde plot
# raw data
#plt.Figure(2)
plt.plot(position_mm, ratio)
plt.ylabel('Ar/Fe')
plt.text(500, 1, 'Raw data, data point: %s' %len(position_mm))
plt.show()

# strategy 1
plt.plot(pos_1, ratio_1)
plt.ylabel('Ar/Fe')
plt.xlabel('Position (mm)')
plt.text(500, 0.01, '$ratio <= 1 \sigma,\ \ MSE<= 1 \sigma $')
plt.text(500, 0.009, 'validity = 1, data point: %s' %len(pos_1))
plt.show()

# strategy 2
plt.plot(pos_2, ratio_2)
plt.ylabel('Ar/Fe')
plt.xlabel('Position (mm)')
plt.text(500, 0.01, '$ratio <= 1 \sigma,\ \ MSE<= 1.5 $')
plt.text(500, 0.009, 'validity = 1, data point: %s' %len(pos_2))
plt.show()

'As result, the strategy 2 can remove reseanable amount of possible crack data'

