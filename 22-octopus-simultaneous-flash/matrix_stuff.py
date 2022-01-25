def get_map_size(matrix):
    return (len(matrix), len(matrix[0]))

def print_map(matrix):
    row_num, row_size = get_map_size(matrix)
    print('=====')
    for i in range(row_num):
        for j in range(row_size):
            print(matrix[i][j], end="")
        print()
    print('=====')

def get_adjacent(matrix, i, j):
    row_num, row_size = get_map_size(matrix)
    adjacent = [
        [i-1, j-1], [i-1, j], [i-1, j+1],
        [i, j-1], [i, j+1],
        [i+1, j-1], [i+1, j], [i+1, j+1]
    ]
    good_adjacent = []

    for point in adjacent:
        if (
            (0 <= point[0] <= row_num-1) and 
            (0 <= point[1] <= row_size-1)
        ):
            good_adjacent.append(point)

    return good_adjacent

def flash(matrix, i, j):
    # mark as flased
    matrix[i][j] = -1
    flash_count = 1
    #print("\t\tFlash!")

    # raise neighbors power level
    adjacent = get_adjacent(matrix, i, j)
    for point in adjacent:
        # if not flashed before
        if matrix[point[0]][point[1]] != -1:
            matrix[point[0]][point[1]] += 1

            # flash the neighbor if power level is high
            if matrix[point[0]][point[1]] > 9:
                flash_count += flash(matrix, point[0], point[1])
    return flash_count


def count_one_step(matrix):
    row_num, row_size = get_map_size(matrix)

    # raise energy level
    for i in range(row_num):
        for j in range(row_size):
            matrix[i][j] += 1

    # count flashes recursively
    flash_count = 0
    for i in range(row_num):
        for j in range(row_size):
            if matrix[i][j] > 9: 
                #print("Starting flash chain. Flash count before: ", flash_count)
                flash_count += flash(matrix, i, j)

    # set flashed energy to zero
    for i in range(row_num):
        for j in range(row_size):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return flash_count


def check_full_sync(matrix):
    row_num, row_size = get_map_size(matrix)
    for line in matrix:
        for item in line:
            if item != 0: return False
    return True

