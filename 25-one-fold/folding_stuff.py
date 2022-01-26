from matrix_stuff import get_matrix_size

def fold_matrix(matrix, folding):
    lines, columns = get_matrix_size(matrix)

    line = folding[1]
    print('Folding:', folding)

    # for v-folding
    if folding[0] == 'y':
        # folding
        for i in range(lines):
            for j in range(columns):
                if i > line and matrix[i][j] == '#':
                    #print("folding [%d][%d]->[%d][%d]" %(i,j,lines-1-i, j))
                    matrix[lines-1-i][j] = matrix[i][j]
        # leave only 1 part
        return matrix[:line]

    # for h-folding
    if folding[0] == 'x':
        # folding
        for i in range(lines):
            for j in range(columns):
                if j > line and matrix[i][j] == '#':
                    #print("folding [%d][%d]->[%d][%d]" %(i,j,i,columns-1-j))
                    matrix[i][columns-1-j] = matrix[i][j]

        # leave only 1 part
        out_matrix = []
        for item in matrix:
            out_matrix.append(item[:line])
        return out_matrix

def get_initial_size(folds):
    first_x = None
    first_y = None
    for item in folds:
        if item[0] == 'x' and not first_x:
            first_x = item[1]
        if item[0] == 'y' and not first_y:
            first_y = item[1]

    return (2*first_y +1, 2*first_x+1)
        
def count_dots(matrix):
    counter = 0
    for line in matrix:
        for j in line:
            if j == '#':
                counter += 1
    return counter
