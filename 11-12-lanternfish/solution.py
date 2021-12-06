
import csv
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')
parser.add_argument('days', metavar='Days', type=int, help='Number of breeding days')

args = parser.parse_args()
infile = vars(args)['infile']
days = vars(args)['days']
print("Infile: %s" %infile)
print("Day number: %s" %days)

# process infile
fishes = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for row in reader:
        for item in row:
            fishes.append(int(item))

birth_cycle = 6
adult_age = 2

buckets = {}

buckets = [0] * (birth_cycle + adult_age +1)

print("Fishes: %s" %fishes)
print("Buckets: %s" %buckets)

for fish in fishes:
    buckets[fish] += 1

print("Buckets with initial fishes:%s" %buckets)

print("                             0  1  2  3  4  5  6  7  8")
mothers = 0
for day in range(days):
    mothers = buckets[0]
    buckets[0] = 0

    for age in range(1, birth_cycle + adult_age + 1):
        buckets[age-1] = buckets[age]
        
    buckets[birth_cycle] += mothers
    buckets[adult_age + birth_cycle] = mothers

    print("After %2d days, buckets are: %s; mothers: %d" %(day+1, buckets, mothers))

fish_sum = 0
for bucket in buckets:
    fish_sum += bucket

print("Fish number: %d" %fish_sum)
