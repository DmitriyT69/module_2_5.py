def get_matrix(n, m, value):
    matrix = []
    row = []
    for i in range(n):
        matrix.append(value)
        for j in range(m):
            row.append(value)
        matrix.append(row)
    print(matrix)
    return matrix

result_1 = get_matrix(2,2,10)
result_2 = get_matrix(3, 5 , 42)
result_3 = get_matrix(4, 2, 13)

print(result_1)
print(result_2)
print(result_3)
