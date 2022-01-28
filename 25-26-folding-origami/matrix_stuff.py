def get_matrix_size(matrix):
    return (len(matrix), len(matrix[0]))

def print_matrix(matrix):
    row_num, row_size = get_matrix_size(matrix)
    print('=====')
    for i in range(row_num):
        for j in range(row_size):
            print(matrix[i][j], end="")
        print()
    print('=====')

