# PyD3

## What is PyD3?

PyD3 is an Implementation of the ID3 (Iterative Dichotomiser 3) algorithm, used to generate a decision tree from a dataset. ID3 is the precursor to the C4.5 algorithm, and is typically used in the machine learning and natural language processing domains.

## How to Access

To run PyD3, clone the repository to the desired directory and set it as your working directory. under src/, run PyD3.py 
`python PyD3.py <path_to_table>`. The .txt table you provide *must* be in the format of:

attribute1, attribute2, attribute3, ..., classifier <br />
data1, data2, data3, ..., classifier_n <br />
datax, datay, dataz, ..., classifier_m <br />
... <br />

Examples of the necessary table format are available in ../sample_tables.

## Output

PyD3 will output a textual representation of the decision tree, along with the time that it took to execute. You can then follow the decision tree to classify tuples.
