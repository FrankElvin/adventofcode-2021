
import csv
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')
parser.add_argument('step_count', metavar='Steps', type=int, help='Number of insertion steps')

args = parser.parse_args()
infile = vars(args)['infile']
step_count = vars(args)['step_count']
print("Infile: %s" %infile)
print("Steps: %s" %step_count)

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

#print("Initial input: ")
#print("template:", template)
#print("insertion:", insertion)

# count unique polymer symbols
symbols = set(insertion.values())
for item in template:
    symbols.add(item)

#print("Unique polymer symbols:", symbols)

def one_step(template, insertion):
    index_addition = 0
    for i in range(len(template)-1):
        pair = template[i+index_addition] + template[i+1+index_addition]

        #print("Working with pair: %s, index: %d" %(pair, i+index_addition))
        if pair in insertion.keys():
            to_insert = insertion[pair]
            template.insert(i+1+index_addition, to_insert)
            index_addition += 1
        else:
            print("Wow. Having pair without insertion rule:", pair)

def get_counts(template, symbols):
    min_res = [None, None]
    max_res = [0, None]
    for char in symbols:
        count = template.count(char)
        if min_res[0]:
            if count < min_res[0]:
                min_res = [count, char]
        else:
            min_res = [count, char]
        if count > max_res[0]:
            max_res = [count, char]
    return min_res, max_res


for i in range(step_count):
    one_step(template, insertion)
    print("Processed step %d. Polymer length: %d" %(i+1, len(template)))

counts = get_counts(template, symbols)
print(counts)
print("Result: %d" %(counts[1][0] - counts[0][0]))
