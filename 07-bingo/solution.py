
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
def main_loop(drawn, boards):
    for number in drawn:
        print("Marking %d" %number)
        position_to_check = mark_in_board(number, boards[0])
        if position_to_check:
            bingo = check_bingo_by_position(boards[0], position_to_check)

        if bingo[0]:
            print_board(boards[0], "First board with bingo!!")
            print("\nBINGO (%s)! On %s %d (number counted from 0)" %(bingo))
            return count_score(board, number)

# DEBUG
#drawn = [20, 18 , 8,  23, 26]
result = main_loop(drawn, boards)
print("Result: %d" %result)
