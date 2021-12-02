
import csv
import argparse
import sys

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

depth = 0
course = 0
print("Initial state: Depth: %d, Course: %d\n" %(depth, course))

with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")

    for row in reader:
        command = row[0]
        value = int(row[1])

        if command == "forward":
            course += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
        else:
            print("Wow! bad/Unexpected input! Row: %s" %row)
            sys.exit(1)

        print("Input: %s %d; Depth: %d, Course: %d" %(command, value, depth, course))


print("\nResult: Depth: %d, Course: %d; Multiplied: %d" %(depth, course, depth*course))
