'''
script to define and provide algorithm for the CART algorithm
author: Caro Strickland
'''

import sys
import os

input_file = open(sys.argv[1], 'r').read().split('\n')

node_dict = [] # will be a list of lists of data tuples
