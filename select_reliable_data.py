#input_name = input()					#是讀取已經covert成csv檔的檔案
import os
import numpy as np

input_file = os.path.expanduser('~/Documents/Python_Training/out.csv')	#python並不會自動展開~/的路徑，所以需要這個指令來展開
with open(input_file, 'r') as f:		#with...as...建立一個區塊中的某指令簡寫，當程式碼離開這個區塊(以對線做區隔)，便自動取消著個指令動作 
	data = []							#故也可做為自動close檔案的一個好方法
	for index, line in enumerate(f):
		if index == 0:
			column_info = line[:-1].split(',')
		else:
			data = data + [line[:-1].split(',')]
for index, value in enumerate(column_info):
    if value == 'Ar':
        ar_col = index
    if value == 'Fe':
        fe_col = index
    if value == 'MSE':
        mse_col = index

ratio = []
mse = []
for datum in data:
    ratio.append(float(datum[ar_col]) / float(datum[fe_col]))	#逐列加入Fe/Ar的比值於ratio中
    mse.append(float(datum[mse_col]))
# identify which points the Ar/Fe value is too high. this may indicate the points are cracks in core.
# leave the points that Ar/Fe value within 2 std of the total Fr/Fe & MSE within 1 std of the total MSE

ratio_std = np.std(ratio)
mse_std = np.std(mse)

output_file = os.path.expanduser('~/Documents/Python_Training/refined.csv')
with open(output_file, 'w') as f:
    #print(column_info, file=f)
    print(column_info, file=f)
    for datum in data:
        cur_ratio = float(datum[ar_col])/float(datum[fe_col])
        if cur_ratio <= ratio_std * 2 and float(datum[mse_col]) <= mse_std:
            print(','.join(datum), file=f)
