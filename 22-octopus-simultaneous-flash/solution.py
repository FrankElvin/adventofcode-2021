
import csv
import argparse

from matrix_stuff import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# process infile
input_data = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        line = []
        for char in row[0]:
            line.append(int(char))
        input_data.append(line)

print("Initial state: ")
print_map(input_data)

step_count = 0
while True:
    step_count += 1
    count_one_step(input_data)
    sync = check_full_sync(input_data)

    if sync == True:
        print("== Step: %d, sync!" %(step_count))
        print_map(input_data)
        break
