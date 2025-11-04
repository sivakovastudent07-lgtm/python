def transpose_matrix(matrix):
    if not isinstance(matrix, list):
        raise TypeError("матрица должна быть списком списков")
    if not matrix:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("каждая строка матрицы должна быть списком")
        if len(row) != cols:
            raise ValueError("все строки матрицы должны быть одинаковой длины")
    
    trans = []
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        trans.append(new_row)
    
    return trans

print("введите матрицу построчно")
print("в каждой строке — числа через пробел (например: 1 2 3 или 3.14 -5 1e2)")
print("введите пустую строку, чтобы завершить ввод")

matrix = []
while True:
    line = input().strip()
    if line == "":
        break
    if not line:
        continue 
    
    row = []
    for part in line.split():
        try:
            row.append(int(part))
        except ValueError:
            try:
                row.append(float(part))
            except ValueError:
                print(f"ошибка: '{part}' не является числом")
                exit()
    matrix.append(row)

if not matrix:
    print("ошибка: матрица пуста")
else:
    first_len = len(matrix[0])
    if any(len(row) != first_len for row in matrix):
        print("ошибка: строки матрицы имеют разную длину")
    else:
        try:
            result = transpose_matrix(matrix)
            print("транспонированная матрица:")
            for row in result:
                print(row)
        except Exception as error:
            print(f"ошибка: {error}")
            