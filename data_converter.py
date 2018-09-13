input_name = input('Input filename: ') #如果需要可以輸入路徑，否則預設都是cmd當下所在的資料夾中的檔案尋找
output_name = input('Output filename: ')
f_in = open(input_name, 'r')
f_out = open(output_name, 'w')
for index, line in enumerate(f_in):		#enumerate是一個同時逐行讀取又會吐出當下是第幾行的指令
	if index >= 2:						#避開results前兩行無用的敘述
		print (','.join(line.split('\t')[1:]), end='', file=f_out)	#將一row的資料以tab做分割並去掉第一columne，在以逗號聯結起來，在寫入先前已經建好的output file 中。
f_in.close()														#end是因enumerate讀入時最後面會自帶/n，如此會造成最終輸出的資料都多隔了一row
f_out.close() #要養成close檔案的習慣，一方面降低記憶體的使用，一方面讓它確實寫入硬碟中，這在執行大型程式時由為重要