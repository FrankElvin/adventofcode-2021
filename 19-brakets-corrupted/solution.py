
import csv
import argparse

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# process infile
input_lines = []
with open(infile, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=" ")
    for row in reader:
        input_lines.append(row[0])


def check_line(line):
    open_brackets = [ '(', '[', '{', '<' ]
    close_brackets = [ ')', ']', '}', '>' ]
    bracket_map = { "(": ")", "[": "]", "{": "}", "<": ">" }

    bracket_stack = []
    error_data = []

    for char in line:
        #print("Checking char: ", char)

        if char in open_brackets:
            bracket_stack.append(char)
            #print("Appended stack: ", bracket_stack)
        elif char in close_brackets:
            if char == bracket_map[bracket_stack[-1]]:
                bracket_stack.pop()
                #print("\tCutted stack: ", bracket_stack)
            else:
                error_data = [ bracket_map[bracket_stack[-1]], char ]
                break
    else:
        return {"result": True, "data": []}

    return {"result": False, "data": error_data}

error_scoring = { ")": 3 , "]": 57, "}": 1197 , ">": 25137 }
def process_result(result):
    if result["result"] == False:
        return error_scoring[ result["data"][1] ]
    else:
        return 0

#print(lines)
full_score = []
for line in input_lines:
    result = check_line(line)
    score = process_result(result)
    full_score.append(score)
    #print('line: %s, result: %s, score: %d' %(line, result, score))

print("Full scoring: %d" %full_score)
print("Middle result: %d" %(sorted(full_score)[len(full_score)//2]))
