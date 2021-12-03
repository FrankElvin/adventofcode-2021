
import csv
import argparse
import sys

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')
parser.add_argument('width', metavar='Width', type=int, help='Width of byte string')

args = parser.parse_args()
infile = vars(args)['infile']
width = vars(args)['width']
print("Infile: %s" %infile)
print("Width: %d" %width)

buckets = []
line_counter = 0
for i in range(width): buckets.append(0)


with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")

    for row in reader:
        byte_string = row[0]

        if len(byte_string) != width:
            print("Entered wrong byte width: %d vs actual %d" %(width, len(byte_string)))
            sys.exit(1)

        for i in range(width):
            buckets[i] += int(byte_string[i])
        line_counter += 1

print("Bucket result: %s; line counter: %d" %(buckets, line_counter))

gamma_rate_bytes = ""
epsilon_rate_bytes = ""
for i in buckets:
    if divmod(line_counter, i)[0] == 1:
        gamma_rate_bytes += "1"
        epsilon_rate_bytes += "0"
    else:
        gamma_rate_bytes += '0'
        epsilon_rate_bytes += '1'
print("Gamma rate bytes: %s, decimal: %d" %(gamma_rate_bytes, int(gamma_rate_bytes, 2)))
print("Epsilon rate bytes: %s, decimal: %d" %(epsilon_rate_bytes, int(epsilon_rate_bytes, 2)))

consumption = int(gamma_rate_bytes, 2) * int(epsilon_rate_bytes, 2) 
print("Consumption: %d" %( consumption))
