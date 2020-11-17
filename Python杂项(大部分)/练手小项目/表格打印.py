tableData=[['apples','oranges','chrtties','banana'],
		   ['Alice','Bob','Carol','David'],
		   ['dogs','cats','moose','goose']]

def printTable(table_data):
	num=0
	k=0
	for i in range(len(table_data)):
		for j in range(len(table_data[i])):
			if len(table_data[i][j])>num:
				num=len(table_data[i][j])
	for i in range(len(table_data)):
		for j in range(len(table_data[i])):
			if k%len(table_data)==0:
				print('\n')
			print(table_data[i][j].rjust(num),end=' ')
			k+=1
printTable(tableData)
print('\n')