def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    trans = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        trans.append(new_row)
    
    return trans
