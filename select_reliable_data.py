# this script is based on the conclusion of select_reliable_data_workflow.py
import os
import numpy as np

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


ratio = []
mse = []

for datum in data:
    ratio.append(float(datum[ar_col]) / float(datum[fe_col]))	#逐列加入Fe/Ar的比值於ratio中
    mse.append(float(datum[mse_col]))

# identify which points the Ar/Fe value is too high. this may indicate the points are cracks in core.
# select the data points whose Ar/Fe value is from 0 to mean + 1 std (83.85% population if normal distributed)
# also the MSE value smaller than 1.5 (practicle experience), and the validity must equal to 1

ratio_std = np.std(ratio)
ratio_mean = np.mean(ratio)
bottom_delet = -10                  #最後10個資料點(以NK-1的1mm解析度來說就是1公分)可能是掃到膠帶，這是需要調整的

refined_data = os.path.expanduser('~/Documents/Python_Training/refined_20180913.csv')
deleted_data = os.path.expanduser('~/Documents/Python_Training/deleted_20180913.csv')
with open(refined_data, 'w') as f:
    with open(deleted_data, 'w') as df:
        cur_ratio = float(datum[ar_col])/float(datum[fe_col])
        print(','.join(column_info), file=f)        #用join可以將list中的物件全部以給予的符號連結起來成為一個字串，故具有iteration的特性
        print(','.join(column_info), file=df)
        for datum in data[:bottom_delet]:
            if cur_ratio <= (ratio_std + ratio_mean) and float(datum[mse_col]) <= 1.5 and datum[vld_col] == '1':
                print(','.join(datum), file=f)  
                #print(datum, file = f)
            else:
                print(','.join(datum), file=df)
        for datum in data[bottom_delet:]:
            print(','.join(datum), file=df)