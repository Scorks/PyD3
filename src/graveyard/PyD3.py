'''
Implementation of the ID3 algorithm
'''
import sys
import math
import operator

table_storage = [] # stores a list of dictionaries representing the table
column_types = [] # stores the names of each column
class_type = sys.argv[2] # the class of the table
base_entropy = 0 # setting the initial base entropy value to 0
class_i = "" # to be set in the base_entropy method - first of the two binary class types
class_ii = "" # to be set in the base_entropy method - second of the two binary class types

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
calculates the initial entropy (info(D))
@data: the table_storage
@ attribute: class type to calculate the entropy with
'''
def base_entropy(data, attribute):
	class_type_i = " " # first of the two binary class types
	class_type_ii = " " # second of the two binary class types
	class_type_i_count = 0 # count for number of binary class I types
	class_type_ii_count = 0 # count for number of binary class II types
	sample_size = len(data) # number of cases in the table

	for item in data:
		if (class_type_i == " "):
			class_type_i = item[attribute]
		elif (class_type_i != item[attribute]):
			class_type_ii = item[attribute]
			break

	# setting the global class_i and class_ii types for future entropy calculations
	global class_i
	global class_ii
	class_i = class_type_i
	class_ii = class_type_ii

	for item in data:
		if (item[attribute] == class_type_i):
			class_type_i_count += 1
		elif (item[attribute] == class_type_ii):
			class_type_ii_count += 1

	# calculate the base entropy value
	equation_section_i = (class_type_i_count/float(sample_size))
	equation_section_ii = (class_type_ii_count/float(sample_size))
	entropy = -1*(math.log(equation_section_i, 2.0)*(equation_section_i) + math.log(equation_section_ii, 2.0)*(equation_section_ii))
	
	return entropy

base_entropy = base_entropy(table_storage, class_type) # sets the base_entropy value to the calculated value

'''
calculates entropy of table 'data' on attribute 'attribute' (info_attribute(D))
@data: the table_storage (altered or unaltered)
@attribute: attribute to calculate the entropy of
'''
def attribute_entropy(data, attribute):
	sample_size = len(data) # total number of entries in the table
	'''
	'attribute_type_dict' is a dictionary with a key value of an attribute type, and a value of a list
	the list has a layout of [a, b, c]
	a = the number of occurances of this type within the attribute
	b = the number of type i within this attribute type
	c = the number of type ii within this attribute type
	'''
	attribute_type_dict = {} # initializing dictionary to hold each different tpye within our attribute as well as their count
	entropy = 0 # entropy which will eventually be returned

	for item in data:
		if item[attribute] not in attribute_type_dict: # if this attribute type is not already in our dictionary...
			attribute_type_dict[item[attribute]] = [1, 0, 0] # add it to the dictionary
			# check whether it is of type i or type ii and set:
			if item[class_type] == class_i:
				attribute_type_dict[item[attribute]][1] = 1
			elif item[class_type] == class_ii:
				attribute_type_dict[item[attribute]][2] = 1
		else:
			attribute_type_dict[item[attribute]][0] = attribute_type_dict[item[attribute]][0] + 1 # increment by 1
			# check whether it is of type i or type ii and set:
			if item[class_type] == class_i:
				attribute_type_dict[item[attribute]][1] = attribute_type_dict[item[attribute]][1] + 1 # increment by 1
			elif item[class_type] == class_ii:
				attribute_type_dict[item[attribute]][2] = attribute_type_dict[item[attribute]][2] + 1 # increment by 1
	for item in attribute_type_dict:
		total_occurances = attribute_type_dict[item][0]
		class_i_occurances = attribute_type_dict[item][1]
		class_ii_occurances = attribute_type_dict[item][2]

		equation_section_i = (class_i_occurances/float(total_occurances))
		equation_section_ii = (class_ii_occurances/float(total_occurances))

		if (equation_section_i == 0.0):
			equation_part_i = 0.0
		else:
			equation_part_i = (equation_section_i * math.log(equation_section_i, 2))
		if (equation_section_ii == 0.0):
			equation_part_ii = 0.0
		else:
			equation_part_ii = (equation_section_ii * math.log(equation_section_ii, 2))
		equation = -1*(total_occurances/float(sample_size))*(equation_part_i + equation_part_ii)
		entropy = entropy + equation # update entropy
		entropy = base_entropy - entropy
	return entropy

'''
returns a set of different types within an attribute
@data: table of data
@attribute: name of the attribute to parse through
'''
def get_attribute_types(data, attribute):
	attribute_types = [] # set to return
	for item in data:
		if item[attribute] not in attribute_types:
			attribute_types.append(item[attribute])
	return attribute_types

'''
returns a table stripped with only the rows of a given attribute type
@data: table of data
@attribute: name of attribute
@attribute_type: attribute types we want to keep within the stripped table
'''
def strip_table(data, attribute, attribute_type):
	return_table = [] # stripped table to return
	for item in data:
		if item[attribute] == attribute_type:
			return_table.append(item)
	return return_table

#-----------------------------------------------------------------------------

def create_tree(data):
	tree_dictionary = {} # final dictionary that will be appended to throughout and returned
	entropy_scores = {} # will store the entropy values for attributes
	attribute_list = column_types # removes the class type from list of attributes
	attribute_list.remove(class_type)

	# discover parent node and add it to tree
	for item in attribute_list:
		entropy_scores[item] = attribute_entropy(data, item)
	root_node = max(entropy_scores.iteritems(), key=operator.itemgetter(1))[0] # find attribute with the highest entropy value
	tree_dictionary[root_node] = get_attribute_types(data, root_node) # adds root node to tree dictionary along with children types
	attribute_list.remove(root_node)
	
	for item in get_attribute_types(data, root_node):
		
		
create_tree(table_storage)
# print attribute_entropy(table_storage, "Education")
