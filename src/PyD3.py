'''
Implementation of the ID3 algorithm
'''
import sys
import math
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
def base_entropy(data):
	class_type_i = " " # first of the two binary class types
	class_type_ii = " " # second of the two binary class types
	class_type_i_count = 0 # count for number of binary class I types
	class_type_ii_count = 0 # count for number of binary class II types
	sample_size = len(data) # number of cases in the table

	for item in data:
		if (class_type_i == " "):
			class_type_i = item[class_type]
		elif (class_type_i != item[class_type]):
			class_type_ii = item[class_type]
			break

	for item in data:
		if (item[class_type] == class_type_i):
			class_type_i_count += 1
		elif (item[class_type] == class_type_ii):
			class_type_ii_count += 1

	# calculate the base entropy value
	equation_section_i = (class_type_i_count/float(sample_size))
	equation_section_ii = (class_type_ii_count/float(sample_size))
	entropy = math.log(equation_section_i, 2.0)*(equation_section_i) + math.log(equation_section_ii, 2.0)*(equation_section_ii)
	
	return entropy


print base_entropy(table_storage)

