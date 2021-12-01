
import csv
import argparse

infile = 'measurements.txt'

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='Csv to process')
args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    prev_value = None
    result = 0

    for row in reader:
        curr_value = int(row[0])

        print("Curr_value: %s, prev_value: %s" %(curr_value, prev_value))

        if not prev_value:
            print("No previous value, moving to the next step")
        else:
            diff = curr_value - prev_value
            print("Found difference: %d" %diff)
            if diff > 0:
                result += 1
        prev_value = curr_value

print("\n\nPositive changes: %d" %result)
