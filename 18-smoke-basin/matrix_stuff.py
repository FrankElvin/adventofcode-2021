
from copy import deepcopy

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

def generate_border_map(matrix):
    new_matrix = deepcopy(matrix)
    row_num, row_size = get_map_size(matrix)
    for i in range(row_num):
        for j in range(row_size):
            if new_matrix[i][j] == 9:
                new_matrix[i][j] = '-'
    return new_matrix


def fill_basin(matrix):
    row_num, row_size = get_map_size(matrix)
    basins = []

    for i in range(row_num):
        for j in range(row_size):
            if matrix[i][j] != '-' and matrix[i][j] != 'x':
                basins.append(get_basin(matrix, i, j))

    return basins
    

def get_basin(matrix, i, j):
    basin_size = 0
    points_to_seek = [ [i,j] ]

    #points_to_seek.extend( get_adjacent(matrix, i, j) )
    print("Initial point: %s (%d,%d)"
            %(matrix[i][j], i, j))

    for point in points_to_seek:
        #print("\tChecking point: %s (%s)" %(matrix[point[0]][point[1]], point))
        basin_size += 1
        new_points = get_adjacent(matrix, point[0], point[1])
        #print("\tNew adjacent: %s" %new_points)
        for new_point in new_points:
            if new_point not in points_to_seek and matrix[new_point[0]][new_point[1]]!='-':
                #print("\t\tAdding new point to basin: %s %s" 
                #       %(matrix[new_point[0]][new_point[1]], new_point))
                points_to_seek.append(new_point)
            #else:
                #print("\t\tNot adding new point to basin: %s %s" 
                #        %(matrix[new_point[0]][new_point[1]], new_point))
    print("Founded basin size: ", basin_size)

    # mark counted basin points
    for point in points_to_seek:
        matrix[point[0]][point[1]] = 'x'

    return basin_size

def get_adjacent(matrix, i, j):
    adjacent = []
    row_num, row_size = get_map_size(matrix)
    if (i != 0):
        adjacent.append([i-1, j])
    if (i != row_num -1):
        adjacent.append([i+1, j])
    if (j != 0):
        adjacent.append([i, j-1])
    if (j != row_size -1):
        adjacent.append([i, j+1])

    return adjacent

