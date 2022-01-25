
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
    repair_brackets = []
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
        for char in bracket_stack[::-1]:
            repair_brackets.append(bracket_map[char]) 
        return {"result": True, "data": [], "repair": repair_brackets}

    return {"result": False, "data": error_data}


def process_result(result):
    completion_scoring = { ')': 1, ']': 2, '}': 3, '>': 4 }

    if result["result"] == True:
        scoring = 0
        for char in result["repair"]:
            scoring *= 5
            scoring += completion_scoring[ char ]
        return scoring
    else:
        return 0

full_score = []
for line in input_lines:
    result = check_line(line)
    score = process_result(result)
    if score > 0: full_score.append(score)
    print('line: %s, result: %s, score: %d' %(line, result, score))
print("Full scoring: %s" %full_score)
print("Target number: %d" %(sorted(full_score)[len(full_score)//2]))
