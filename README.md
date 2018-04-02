# PyD3

## What is PyD3?

PyD3 is an Implementation of the ID3 (Iterative Dichotomiser 3) algorithm, used to generate a decision tree from a dataset. ID3 is the precursor to the C4.5 algorithm, and is typically used in the machine learning and natural language processing domains.

## How to Access

### Open via GUI

To run PyD3 via a GUI, ensure that the path to PyD3.py is executable. To do this, perform the following commands in the command line: <br />
`chmod +x PyD3.py` <br />
`export PATH=/path/to/script:$PATH` <br />
Then, you can run the command:
`python main.py <path_to_table>` <br />
This will open the Tkinter GUI and provide a scrollable version of the ID3 decision tree.


### Open via Command Line

To run PyD3, clone the repository to the desired directory and set it as your working directory. under src/, run PyD3.py 
`python PyD3.py <path_to_table>`. The .txt table you provide *must* be in the format of:

attribute_1, attribute_2, attribute_3, ..., classifier <br />
data_1, data_2, data_3, ..., classifier_n <br />
data_x, data_y, data_z, ..., classifier_m <br />
... <br />

Examples of the necessary table format are available in ../sample_tables.

## Output

PyD3 will output a textual representation of the decision tree, along with the time that it took to execute. You can then follow the decision tree to classify tuples.
