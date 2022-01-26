
import csv
import argparse

from matrix_stuff import *
from folding_stuff import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# process infile
dots = []
folds = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        if row:
            if not row[0].startswith('fold'):
                dots.append([int(row[0]), int(row[1])])
            else:
                folds.append([row[0].split(' ')[-1].split('=')[0],
                   int(row[0].split(' ')[-1].split('=')[1])
                ])

print("Initial input: ")
#print("Dots:", dots)
#print("Folds:", folds)

# !!! this is important. Size can be less than the maximum input coordinate
height, width = get_initial_size(folds)
print("Matrix size: height %d x width %d" %(height, width))

matrix = []
for i in range(height):
    row = ['.'] * width
    matrix.append(row)

#print_matrix(matrix)
for dot in dots:
    matrix[dot[1]][dot[0]] = '#'

#print_matrix(matrix)
for fold in folds:
    matrix = fold_matrix(matrix, fold)
    #print_matrix(matrix)
print_matrix(matrix)
print("Dots in the result: %d" %count_dots(matrix))
