import numpy as np
import math

class Node:
    def __init__(self, attribute):
        self.attribute = attribute # attribute type of the node
        self.children = [] # children of the selected node
        self.classification = "" # classifier for node
        
    def __str__(self):
        return self.attribute

def create_node(data, attributes):
	
    if (np.unique(data[:, -1])).shape[0] == 1:
        node = Node("")
        node.answer = np.unique(data[:, -1])[0]
        return node
        
    gains = np.zeros((data.shape[1] - 1, 1))
    
    for col in range(data.shape[1] - 1):
        gains[col] = gain_ratio(data, col)
        
    split = np.argmax(gains)
    
    node = Node(metadata[split])    
    metadata = np.delete(metadata, split, 0)    
    
    items, dict = subtables(data, split, delete=True)
    
    for x in range(items.shape[0]):
        child = create_node(dict[items[x]], metadata)
        node.children.append((items[x], child))
    
    return node   

def empty(size): # prints the tabbing for tables
    spaces = ""
    for x in range(size):
        spaces += "   "
    return spaces
