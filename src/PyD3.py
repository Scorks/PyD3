import numpy as np
import csv
import math
import sys
import io
import time

'''
Node class that encapsulates the information about all nodes in the tree

@attribute: the attribute type
@children: children of this node
@classification: boolean value for the classifier
'''
class Node:
    def __init__(self, attribute):
        self.attribute = attribute # attribute type of the node
        self.children = [] # children of the selected node
        self.classification = "" # classifier for node
        
    def __str__(self):
        return self.attribute

def get_width(arr):
    count = 0
    for item in arr:
        count = count + 1
    return count

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

def create_subtable(data, attribute, delete_bool):
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
        if delete_bool:
            attribute_dict[items[x]] = np.delete(attribute_dict[items[x]], attribute, 1)
        
    return items, attribute_dict
        

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
Performs the information gain calculations and returns the index
of the selected attribute

@data: data set we are looking at 
'''
def get_information_gain(data, attribute):
    items, dict = create_subtable(data, attribute, False)

    total_size = get_width(data)
    entropies = np.zeros((get_width(items), 1))
    intrinsic = np.zeros((get_width(items), 1))
    
    for x in range(get_width(items)):
        ratio = get_width(dict[items[x]])/(total_size * 1.0)
        entropies[x] = ratio * get_entropy(dict[items[x]][:, -1])
        intrinsic[x] = ratio * math.log(ratio, 2)
        
    total_entropy = get_entropy(data[:, -1])
    iv = -1 * sum(intrinsic)
    
    for x in range(get_width(entropies)):
        total_entropy -= entropies[x]
        
    return total_entropy / iv


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

    maxval = 0
    for n in gain_values:
        if (n > maxval):
            maxval = n
    i = np.where(gain_values == maxval)
    split_value = i[0][0]
    
    node = Node(attributes[split_value])
    attributes = np.delete(attributes, split_value, 0)  

    items, dict = create_subtable(data, split_value, True)

    for x in range(get_width(items)):
        child_node = create_node(dict[items[x]], attributes)
        node.children.append((items[x], child_node))
    
    return node

# prints the tabbing for tables
def indentation(size):
    spaces = ""
    for x in range(size):
        spaces += "   "
    return spaces

def tree(node, level):
    if (node.classification != ""): # if node IS a leaf node
        print indentation(level), node.classification
        return

    print indentation(level), node.attribute

    for value, i in node.children:
        print indentation(level + 1), value
        tree(i, level + 2)

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

    node = create_node(reformed_data, column_types)

    tree(node, 0)

# MAIN METHOD----------------------------------------------------------------

start_time = time.time()
run()
print "\n"
print "Time Elapsed: ", ("%s seconds" % (time.time() - start_time))
