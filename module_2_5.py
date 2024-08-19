def get_matrix(n, m, value):
    matrix = []
    for i in range(0, int(n)):
        a = []
        matrix.append(a)
        for j in range(0, int(m)):
            a.append(value)
    return matrix


get_matrix('2', '2', '10', )
result1 = get_matrix('2', '2', '10')
print(result1)
get_matrix('3', '5', '42')
result2 = get_matrix('3', '5', '42')
print(result2)
get_matrix('4', '2', '13')
result3 = get_matrix('4', '2', '13')
print(result3)