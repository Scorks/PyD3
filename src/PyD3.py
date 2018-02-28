'''
Implementation of the ID3 algorithm
'''
import sys
import csv
import sqlite3

table_storage = [] # stores a list of dictionaries representing the table
column_types = [] # stores the names of each column
class_type = sys.argv[2] # the class of the table

# resolve the column types
with open(sys.argv[1]) as f:
    column_line = f.readline()
    column_line = column_line.split()
    column_types = column_line

input_file = open(sys.argv[1], 'r').read().split('\n') # input table

#-----------------------------------------------------------------------------

for line in iter(input_file):
	line = line.split()
	if line:
		temp_dict = {}
		for item in column_types:
			temp_dict[item] = line[column_types.index(item)]
		table_storage.append(temp_dict)
del table_storage[0] # remove the list of just column types


#-----------------------------------------------------------------------------

'''
calculate the initial entropy
@data: the table_storage
'''
def entropy(data):
	class_type_i = " " # first of the two binary class types
	class_type_ii = " " # second of the two binary class types
	for item in data:
		if (class_type_i == " "):
			class_type_i = item[class_type]
		elif (class_type_i != item[class_type]):
			class_type_ii = item[class_type]
			break
	sample_size = len(table_storage) # number of cases in the table
	

entropy(table_storage)

