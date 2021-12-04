
def print_board(board, caption):
    print("board %s" %caption)
    for line in board:
        for item in line:
            print(item, end=" | ")
        print()

def mark_in_board(number, board):
    for line in board:
        for item in line:
            if item.is_equal(number):
                item.mark()

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

def check_bingo_board(board):
    """Check if a board contains bingo"""
    board_size = len(board)
    print("Checking board for bingo")
    print_board(board, "")

    for i in range(board_size):
        # checking the first line items for maybe bingo columns
        if board[0][i].is_marked():
            result = check_bingo_one(board, i, 'column')
            print("\tChecking column %d: %s" %(i+1, result))
            if result:
                return result, 'column', i

        # checking the first column items for maybe bingo lines
        if board[i][0].is_marked():
            result = check_bingo_one(board, i, 'line')
            print("\tChecking line %d: %s" %(i+1, result))
            if result:
                return result, 'line', i

    print("No bingo for now")
    return False, None, None

def count_score(board, last_draw):
    board_sum = 0
    for line in board:
        for item in line:
            if not item.is_marked(): board_sum += item.value
    return board_sum * last_draw
