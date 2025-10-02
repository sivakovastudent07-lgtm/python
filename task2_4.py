def transpose_matrix(matrix):
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    for row in matrix:
        if len(row) != cols:
            raise ValueError("все строки матрицы должны быть одинаковой длины")
    
    trans = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        trans.append(new_row)
    
    return trans