#!/usr/bin/env python

import numpy as np
import csv
import math
import sys
import io
import time
from Tkinter import *

'''
Node class that encapsulates the information about all nodes in the tree

@attribute: the attribute type
@children: children of this node
@classification: boolean value for the classifier
'''
class Node:
    def __init__(self, attribute):
        self.children = [] # children of the selected node
        self.classification = "" # classifier for node
        self.attribute = attribute # attribute type of the node
        
    def __str__(self):
        return self.attribute

'''
gets the width of a 2-dimensional NP array (number of rows)

@arr: Numpy array
'''
def get_width(arr):
    count = 0
    for item in arr:
        count = count + 1
    return count

'''
gets the length of a 2-dimensional NP array (number of columns)

@arr: Numpy array
'''
def get_length(arr):
    count = 0
    for item in arr[0]:
        count = count + 1
    return count

'''
checks if a node should have a classification value (binary true/false)

@data: data set we are looking at
'''
def leaf_check(data):
    if (get_width(np.unique(data[:, -1]))) == 1:
        return True
    else:
        return False

'''
splits a table based on a provided NP table and the attribute in which to split

@data: data set we are looking at
@attribute: attribute to split on
@delete_bool: where we delete items or not
'''
def split_table(data, attribute, delete_bool):
    attribute_dict = {}
    items = np.unique(data[:, attribute])
    count = np.zeros((get_width(items), 1), dtype=np.int32) 

    for x in range(get_width(items)):
        for y in range(get_width(data)):
            if data[y][attribute] == items[x]:
                count[x] += 1

    for x in range(get_width(items)):
        attribute_dict[items[x]] = np.empty((count[x], get_length(data)), dtype="|S32")
        index = 0
        for y in range(get_width(data)):
            if data[y, attribute] == items[x]:
                attribute_dict[items[x]][index] = data[y]
                index += 1       
        if delete_bool == True:
            attribute_dict[items[x]] = np.delete(attribute_dict[items[x]], attribute, 1)
        
    return items, attribute_dict
        

'''
performs the information gain calculations and returns the index
of the selected attribute

@data: data set we are looking at 
'''
def get_information_gain(data, attribute):
    items, dict = split_table(data, attribute, False)

    total_size = get_width(data)
    entropy_list = np.zeros((get_width(items), 1))
    
    for x in range(get_width(items)):
        multiplication_factor = get_width(dict[items[x]])/(total_size * 1.0)
        entropy_list[x] = multiplication_factor * get_entropy(dict[items[x]][:, -1])
        
    total_entropy = get_entropy(data[:, -1])
    
    for x in range(get_width(entropy_list)):
        total_entropy -= entropy_list[x]
        
    return total_entropy

'''
helper method for get_information_gain to split up the mathematical tasks into
smaller subsections

@X: classifier value(s)
'''
def get_entropy(X):
    items = np.unique(X)

    if items.size == 1: # checks if all true or all false
        return 0

    counts = np.zeros((items.size, 1))
    sums = 0

    for x in range(get_width(items)):
        counts[x] = sum(X == items[x]) / (X.size * 1.0)

    for item in counts:
        sums += item * -1 * math.log(item, 2)

    return sums

'''
recusrive method to create a set of nodes that will store data essential
to building the final ID3 decision tree

@data: the data set we are looking at
@attributes: the list of attributes (first line in the input table)
'''
def create_node(data, attributes):
    if leaf_check(data):
        node = Node("") # create a new node
        # sets the classification value to the first item in the list
        node.classification = np.unique(data[:, -1])[0]
        return node
    
    #calculating gain values
    gain_values = np.zeros((get_length(data) - 1, 1))
    for column in range(get_length(data) - 1):
        gain_values[column] = get_information_gain(data, column)

    '''
    maxval = 0
    for n in gain_values:
        if (n > maxval):
            maxval = n
    i = np.where(gain_values == maxval)
    split_value = i[0][0]
    '''

    split_value = np.argmax(gain_values)
    
    node = Node(attributes[split_value])
    attributes = np.delete(attributes, split_value, 0)  

    items, dict = split_table(data, split_value, True)

    for x in range(get_width(items)):
        child_node = create_node(dict[items[x]], attributes)
        node.children.append((items[x], child_node))
    
    return node

'''
recusrive function responsible for building a textual representation of
the final ID3 decision tree by printing out essential node information at
different indented levels

@node: starting Node
@level: the level of the tree that we are currently at (for indentation purposes)
'''
def tree(node, level):
    spaces = ""
    if (node.classification != ""): # if node IS a leaf node
        for x in range(level):
            spaces += "   "
        print spaces, node.classification
        return

    spaces = ""
    for x in range(level):
        spaces += "   "
    print spaces, node.attribute

    spaces = ""
    for value, i in node.children:
        for x in range(level + 1):
            spaces += "   "
        print spaces, value
        spaces = ""
        tree(i, level + 2)

'''
method to help declutter tha main method, takes in a file in a specific format
and converts it into a numpy array that we can work with - also begins the
method to start building the ID3 decision tree
'''
def run():
    with open(sys.argv[1]) as f:
        column_line = f.readline()
        column_line = column_line.split(",")
        column_types = column_line

    with open(sys.argv[1], 'r') as f:
        CSV_datareader = csv.reader(f, delimiter=',')
        data = []

        for row in CSV_datareader:
            data.append(row)

    del data[0]   
    reformed_data = np.array(data)

    start_node = create_node(reformed_data, column_types)

    tree(start_node, 0)

# MAIN METHOD----------------------------------------------------------------

start_time = time.time()
run()
print "\n"
print "Time Elapsed: ", ("%s seconds" % (time.time() - start_time))

