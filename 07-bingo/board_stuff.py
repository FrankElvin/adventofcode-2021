
def print_board(board, caption):
    print("board %s" %caption)
    for line in board:
        for item in line:
            print(item, end=" | ")
        print()

def mark_in_board(number, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].is_equal(number):
                board[i][j].mark()
                print("Marking line: %d; column: %d" %(i, j))
                return (i, j)
    return None

def check_bingo_one(board, index, linetype):
    """Check if line or column is a BINGO line or column"""
    result = True
    if linetype == 'column':
        for i in range(len(board[index])):
            if not board[i][index].is_marked():
                result = False
                break
    else:
        for i in range(len(board)):
            if not board[index][i].is_marked():
                result = False
                break
    return result

def check_bingo_by_position(board, position_to_check):
    """Check if a board contains bingo by updated position"""
    board_size = len(board)
    print("Checking board for bingo")
    print_board(board, "")

    line_res = check_bingo_one(board, position_to_check[0], 'line')
    print("\tChecking line %d: %s" %(position_to_check[0]+1, line_res))
    if line_res:
        return line_res, 'line', position_to_check[0]

    column_res = check_bingo_one(board, position_to_check[1], 'column')
    print("\tChecking column %d: %s" %(position_to_check[1]+1, column_res))
    if column_res:
        return column_res, 'column', position_to_check[1]

    print("No bingo for now")
    return False, None, None


def count_score(board, last_draw):
    board_sum = 0
    for line in board:
        for item in line:
            if not item.is_marked(): board_sum += item.value
    return board_sum * last_draw
