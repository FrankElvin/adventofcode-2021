
import csv
import argparse

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

for row in floor_map:
    for x in row:
        print(x, end='')
    print()

row_num = len(floor_map)
row_size = len(floor_map[0])
print("Map size: %d x %d" %(row_num, row_size))

def check_low_point(i, j, matrix):
    row_num = len(matrix)
    row_size = len(matrix[0])

    #print("\tChecking point: %d (%d, %d)" %(matrix[i][j], i, j))
    adjacent = []

    if (i != 0):
        adjacent.append(matrix[i-1][j])
    if (i != row_num -1):
        adjacent.append(matrix[i+1][j])

    if (j != 0):
        adjacent.append(matrix[i][j-1])
    if (j != row_size -1):
        adjacent.append(matrix[i][j+1])

    #print("\tAdjacent: %s" %adjacent)

    if matrix[i][j] < min(adjacent):
        return True
    else:
        return False

overall_risk = 0
for i in range(row_num):
    for j in range(row_size):
        if check_low_point(i, j, floor_map):
            overall_risk += 1 + floor_map[i][j]

print("Overall risk: %d" %overall_risk)
