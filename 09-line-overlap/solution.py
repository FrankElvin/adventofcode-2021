
import csv
import argparse
import sys
import copy

from VentPoint import VentPoint
from diagram_stuff import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# read initial data array
def read_points(coords):
    points = coords.split(',')
    for i in range(2):
        points[i] = int(points[i])
    return points

lines = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")

    for row in reader:
        line = []
        line.append(read_points(row[0]))
        line.append(read_points(row[2]))
        lines.append(line)

for line in lines:
    print(line)

# filtering out non-horizontal and non-vertical lines
straight_lines = []
for line in lines:
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        straight_lines.append(line)
lines = straight_lines

print()
for line in straight_lines:
    print(line)

diagram = init_vent_diagram(10)
print_diagram(diagram)

#for line in lines:
#    mark_line(diagram, line)
#
#print_diagram(diagram)
