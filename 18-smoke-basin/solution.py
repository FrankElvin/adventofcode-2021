
import csv
import argparse

from matrix_stuff import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# process infile
floor_map = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        map_row = []
        for char in row[0]:
            map_row.append(int(char))

        floor_map.append(map_row)

print_map(floor_map)
print("Map size: %d x %d" %get_map_size(floor_map))

border_map = generate_border_map(floor_map)
print_map(border_map)

basins = fill_basin(border_map)
print_map(border_map)

big_basins = sorted(basins, reverse=True)[:3]
result = 1
for basin in big_basins:
    result *= basin
print("Result: ", result)

