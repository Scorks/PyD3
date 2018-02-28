'''
Implementation of the ID3 algorithm
'''
import sys
import csv
import sqlite3

table_storage = [] # stores a list of dictionaries representing the table
column_types = [] # stores the names of each column

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
		# TODO: CREATE LIST OF DICTS FOR TABLE STORAGE