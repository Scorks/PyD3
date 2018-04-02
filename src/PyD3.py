import numpy as np
import math
import sys
import io

class Node:
    def __init__(self, attribute):
        self.attribute = attribute # attribute type of the node
        self.children = [] # children of the selected node
        self.classification = "" # classifier for node
        
    def __str__(self):
        return self.attribute
    
'''
checks if a node should have a classification value (binary true/false)

@data: data set we are looking at
'''
def leaf_check(data):
    if (np.unique(data[:, -1])).size == 1:
        return True
    else:
        return False

def create_subtable(data, attribute, delete_bool):
    attribute_dict = {}
    count = np.zeros((items.shape[0], 1), dtype=np.int32) 
    items = np.unique(data[:, attribute]) # collect all unique specific attribute items
    
    for x in range(items.shape[0]):
        for y in range(data.shape[0]):
            if data[y][attribute] == items[x]:
                count[x] += 1

    for x in range(items.shape[0]):
        attribute_dict[items[x]] = np.empty((count[x], data.shape[1]), dtype="|S32")
        index = 0
        for y in range(data.shape[0]):
            if data[y, attribute] == items[x]:
                attribute_dict[items[x]][index] = data[y]
                index += 1       
        if delete_bool:
            attribute_dict[items[x]] = np.delete(attribute_dict[items[x]], attribute, 1)
        
    return items, attribute_dict
        

def entropy(X):
    items = np.unique(X)

    if items.size == 1: # checks if all true or all false
        return 0

    counts = np.zeros((items.size, 1))
    sums = 0

    for x in range(items.size):
        counts[x] = sum(X == items[x]) / (X.size * 1.0)

    for item in counts:
        sums += item * -1 * math.log(count, 2)

    return sums

'''
Performs the information gain calculations and returns the index
of the selected attribute

@data: data set we are looking at 
'''
def information_gain(data, attribute):
    items, dict = create_subtable(data, attribute, False)





def create_node(data, attributes):
    if leaf_check(data):
        node = Node("") # create a new node
        # sets the classification value to the first item in the list
        node.classification = np.unique(data[:, -1])[0]
        return node
    
    #calculating gain values
    gain_values = np.zeros((data.shape[1] - 1, 1))

    for column in range(data.shape[1] - 1):
        gain_values[column] = information_gain(data, column)

    maxval = 0
    for n in gains:
        if (n > maxval):
            maxval = n
    i = np.where(gains == maxval)
    split_value = i[0][0]
    
    node = Node(attributes[split_value])
    attributes = np.delete(attributes, split_value, 0)  

    items, dict = create_subtable(data, split_value, True)

    for x in range(items.shape[0]):
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
    
    data = []
    with open(sys.argv[1], "r") as f:
        sentences = [elem for elem in f.read().split('\n') if elem]
        for sentence in sentences:
            data.append(sentence.split(","))
        del data[0]

    reformed_data = np.array(data)
    node = create_node(reformed_data, column_types)

    tree(node, 0)

# MAIN METHOD----------------------------------------------------------------

run()
