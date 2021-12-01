
import csv
import argparse

infile = 'measurements.txt'

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')
parser.add_argument('window_size', metavar='Window', type=int, help='Window size')

args = parser.parse_args()
infile = vars(args)['infile']
window_size = vars(args)['window_size']
print("Infile: %s" %infile)
print("Sliding window size: %d" %window_size)

prev_sum = None
result = 0
window_data = []

print("Initial state of window data: ", window_data)

with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    for row in reader:
        curr_value = int(row[0])

        if (len(window_data)<window_size):
            print("Adding new empty window to the window data")
            window_data.append([])

        for window in window_data:
            window.append(curr_value)

        print("Read value: %s, window_data: %s" %(curr_value, window_data))

        #for i in range(len(window_data)):
        #    window_data[i].append(curr_value)
        #    if len(window_data[i] == window_size):

        if len(window_data) == window_size:
            curr_window = window_data.pop(0)
            curr_sum = sum(curr_window)
            print("Popped window: %s, sum: %d" %(curr_window, curr_sum))
            window_data.append([])

            print("Popped window: %s, sum: %d, prev_sum: %s" %(curr_window, curr_sum, prev_sum))
            if prev_sum:
                diff = curr_sum - prev_sum
                print("Found difference: %d" %diff)
                if diff > 0:
                    result += 1
            
            prev_sum = curr_sum

print("\n\nPositive changes: %d" %result)
