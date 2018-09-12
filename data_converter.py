input_name = input('Input filename: ')
output_name = input('Output filename: ')
f_in = open(input_name, 'r')
f_out = open(output_name, 'w')
for index, line in enumerate(f_in):
	if index >= 2:
		print (','.join(line.split('\t')[1:]), end='', file=f_out)
f_in.close()
f_out.close()