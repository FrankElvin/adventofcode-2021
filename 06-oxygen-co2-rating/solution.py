
import csv
import argparse
import sys
import copy

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

data = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        data.append(row[0])

def print_data(data, header):
    print("%s" %header)
    for line in data:
        print("\t", line)

def get_by_criteria(data, position, gas):
    line_counter = len(data)
    position_result = 0
    for line in data:
        position_result += int(line[position])

    #print("\t1 number in position %d: %d; lines: %d" %(position, position_result, line_counter))

    # if bytes are equal in number
    co2_rating = None
    oxygen_rating = None
    if (
        divmod(line_counter, position_result)[0] == 2 and 
        divmod(line_counter, position_result)[1] == 0
    ):
        oxygen_rating = 1
        co2_rating = 0
    # 1 is more common
    elif divmod(line_counter, position_result)[0] == 1:
        oxygen_rating = 1
        co2_rating = 0
    # 0 is more common
    else:
        oxygen_rating = 0
        co2_rating = 1

    #print("\tPosition: %d, o2: %d, co2: %d" %(position, oxygen_rating, co2_rating))
    oxygen_lines = []
    co2_lines = []

    for line in data:
        if oxygen_rating == 1:
            if line[position] == "1": oxygen_lines.append(line)
            else: co2_lines.append(line)
        else:
            if line[position] == "0": oxygen_lines.append(line)
            else: co2_lines.append(line)

    if gas == "oxygen":
        return oxygen_lines
    else:
        return co2_lines

def get_gas_criteria(data, gas):
    o2 = copy.deepcopy(data)
    counter = 0
    print("Counting criteria for %s" %gas)
    while True:
        o2 = get_by_criteria(o2, counter, gas)
        if len(o2) == 1:
            o2_number = int(o2[0], 2)
            return o2_number
        else:
            print("\tLevel %d. Going one level deeper" %counter)
            counter += 1


o2_number = get_gas_criteria(data, "oxygen")
co2_number = get_gas_criteria(data, "co2")
print("Oxygen rating: %d, CO2 rating: %d" %(o2_number, co2_number))
print("Result: %d" %(o2_number * co2_number))
