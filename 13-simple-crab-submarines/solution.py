
import csv
import argparse

from crab_functions import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# process infile
crabs = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        for item in row:
            crabs.append(int(item))

print("Crabs: %s" %crabs)

target_ranges = range(min(crabs), max(crabs))
costs = []

print("Target position in range %s" %target_ranges)

for target_range in target_ranges:
    costs.append(get_fuel_consumption(crabs, target_range))

optimal_pair = None
for item in zip(target_ranges, costs):
    if not optimal_pair:
        optimal_pair = item
    else:
        if optimal_pair[1]>item[1]:
            optimal_pair = item
    print("Range: %d, cost: %d" %(item[0], item[1]))

print("Optimal pair: %d %d" %optimal_pair)

#print("\nTotal Consumption: %d" %cons)
