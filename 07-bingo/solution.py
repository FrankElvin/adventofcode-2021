
import csv
import argparse
import sys
import copy

from BoardNumber import BoardNumber
from board_stuff import *

parser = argparse.ArgumentParser(description='Read input file')
parser.add_argument('infile', metavar='Infile', type=str, help='File to process')

args = parser.parse_args()
infile = vars(args)['infile']
print("Infile: %s" %infile)

# read initial data array
drawn = []
boards = []
with open(infile, 'r') as csvfile:
    x = csvfile.readline()[:-1].split(',')
    for value in x:
        drawn.append(int(value))
    print(drawn)
    board = []

    for line in csvfile.readlines():
        if line == "\n":
            if board:
                boards.append(board)
                board = []
        else:
            board_line = []
            numbers = line[:-1].split()
            for x in numbers:
                board_line.append(BoardNumber(int(x), False))
            board.append(board_line)
    else:
        boards.append(board)

# DEBUG
boards = [ boards[2] ]

for board in boards:
    print_board(board, '')

# draw numbers one by one and check bingo every time
for number in drawn:
    print("Marking %d" %number)
    mark_in_board(number, boards[0])
    bingo = check_bingo_board(board)
    if bingo[0]:
        break

print("\nBINGO (%s)! On %s %d (number counted from 0)" %(bingo))
print("Result: %d" %(count_score(board, number)))
