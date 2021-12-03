
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

# one iteration of processing binary data
def get_by_criteria(data, position, gas):
    line_counter = len(data)
    position_result = 0
    for line in data:
        position_result += int(line[position])

    # if bytes are equal in number
    co2_rating = None
    oxygen_rating = None
    if (
        divmod(line_counter, position_result)[0] == 2 and 
        divmod(line_counter, position_result)[1] == 0
    ):
        oxygen_rating = 1
        co2_rating = 0
    # 1 is more common in the specified position
    elif divmod(line_counter, position_result)[0] == 1:
        oxygen_rating = 1
        co2_rating = 0
    # 0 is more common in the specified position
    else:
        oxygen_rating = 0
        co2_rating = 1

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
    gas_data = copy.deepcopy(data)
    counter = 0
    print("Counting criteria for %s" %gas)
    while True:
        gas_data = get_by_criteria(gas_data, counter, gas)
        if len(gas_data) == 1:
            return int(gas_data[0], 2)
        else:
            print("\tLevel %d. Going one level deeper" %counter)
            counter += 1



# read initial data array
data = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        data.append(row[0])

o2_number = get_gas_criteria(data, "oxygen")
co2_number = get_gas_criteria(data, "co2")
print("Oxygen rating: %d, CO2 rating: %d" %(o2_number, co2_number))
print("Result: %d" %(o2_number * co2_number))
