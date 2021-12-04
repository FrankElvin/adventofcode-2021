
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

# draw numbers one by one and check bingo every time
def main_loop(drawn, boards):
    print("Running bingo for %d boards" %(len(boards)))

    print("First 5 numbers - for starters: ", drawn[:5])
    for number in drawn[:5]:
        print("Marking %d" %number)
        for board in boards:
            mark_in_board(number, board)

    print("Here starts the BINGO game: ", drawn[5:])
    for number in drawn[5:]:
        lost_boards = []
        boards_in_game = []

        print("Marking %d" %number)
        print("\tBoards in game: %d" %(len(boards)))
        for i in range(len(boards)):
            board = boards[i]
            marked = mark_in_board(number, board)
            if marked:
                bingo = check_bingo_by_position(board, marked)
                if bingo:
                    #print("\t\tBingo!")
                    lost_boards.append(board)
                else:
                    #print("\t\tNot Bingo!")
                    boards_in_game.append(board)
            else:
                #print("\t\tEven not marked the number!")
                boards_in_game.append(board)

        
        if len(lost_boards) !=0:
            print("\tBoards with bingo: %d" %(len(lost_boards)))

        if len(boards_in_game) == 1:
            print("\tWe found the last board in game. Keeping calling numbers.")

        elif len(boards_in_game) == 0:
            print("\nAll boards passed away. getting last passed board")
            return lost_boards[-1], number

        boards = boards_in_game

result = main_loop(drawn, boards)
print_board(result[0], '')
print("Result: %d" %(count_score(result[0], result[1])))
