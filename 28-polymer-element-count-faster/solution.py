
import csv
import argparse
import sys

from step_stuff import add_to_buckets, one_step
from count_stuff import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')
parser.add_argument('step_count', metavar='Steps', type=int, help='Number of insertion steps')

args = parser.parse_args()
infile = vars(args)['infile']
step_count = vars(args)['step_count']
print("Infile: %s" %infile)
print("Steps: %s" %step_count)

sys.setrecursionlimit(5000)

# process infile
template = []
insertion = {}
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        if row:
            if len(row) == 1:
                for char in row[0]:
                    template.append(char)
            else:
                insertion[row[0]] = row[2]

print("Initial input: ")
print("template:", template)
print("insertion:", insertion)

# count unique polymer symbols
symbols = set(insertion.values())
for item in template:
    symbols.add(item)
print("Unique polymer symbols:", symbols)

buckets = {}
for i in range(len(template)-1):
    pair = template[i] + template[i+1]
    if pair in buckets.keys():
        buckets[pair] += 1
    else:
        buckets[pair] = 1
print("Initial buckets:", buckets, "\n")

for i in range(step_count):
    print("======================")
    buckets = one_step(buckets, insertion)
    print("Processed step %d. Buckets: %s" %(i+1, buckets))

print("======================")


repair_result = repair_polymer(buckets)
print("Repair result:", repair_result)
if (repair_result[1]):
    print("The polymer is repaired successfully")
    counts = get_counts(repair_result[0], symbols)
    print(counts)
    print("Result: %d" %(counts[1][0] - counts[0][0]))
    
