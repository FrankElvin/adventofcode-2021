
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
#boards = [ boards[2] ]
#for board in boards:
#    print_board(board, '')

# draw numbers one by one and check bingo every time
def main_loop(drawn, boards):

    print("First 5 numbers - for starters: ", drawn[:5])
    for number in drawn[:5]:
        print("Marking %d" %number)
        for board in boards:
            mark_in_board(number, board)

    print("Here starts the BINGO game: ", drawn[5:])
    for number in drawn[5:]:
        print("Marking %d" %number)
        for board in boards:
            marked = mark_in_board(number, board)
            if marked:
                bingo = check_bingo_by_position(board, marked)

                if bingo:
                    print_board(board, "First board with bingo!!")
                    print("\nBINGO (%s)! On %s %d (number counted from 0)" %(bingo))
                    return count_score(board, number)

# DEBUG
result = main_loop(drawn, boards)
print("Result: %d" %result)
