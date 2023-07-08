# Напишите функцию для транспонирования матрицы

def transposition_func(matrix: list) -> list:
    zipped_rows = zip(*matrix)
    transposition_matrix = [list(row) for row in zipped_rows]
    return transposition_matrix


my_matrix = [[1, 2, 3], [4, 5, 6]]
print(transposition_func(my_matrix))













