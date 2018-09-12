#input_name = input()					#是讀取已經covert成csv檔的檔案
import os

path = os.path.expanduser('~/Documents/Python_Training/out.csv')
with open(path, 'r') as f:		#with...as...建立一個區塊中的某指令簡寫，當程式碼離開這個區塊(以對線做區隔)，便自動取消著個指令動作 
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
ratio = []
for datum in data:
	ratio.append(float(datum[fe_col]) / float(datum[ar_col]))	#逐列加入Fe/Ar的比值於ratio中
sorted_ratio = sorted(ratio)
max_diff = -1
for index, value in enumerate(sorted_ratio[:-2]):
	diff = sorted_ratio[index + 1] - value
	if diff > max_diff:
		max_diff = diff
		max_index = index
threshold = (sorted_ratio[max_index] + sorted_ratio[max_index + 1]) / 2
output_name = input()
with open(output_name, 'w') as f:
	print (','.join(column_info), file=f)
	for datum in data:
		cur_ratio = float(datum[fe_col]) / float(datum[ar_col])
		if cur_ratio > threshold:
			print (','.join(datum), file=f)
