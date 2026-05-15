matrix = [
    [2, 5, 7, 3],
    [4, 1, 8, 6],
    [3, 9, 2, 5],
    [6, 4, 1, 7]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

matrix_cubed = [[row[0]**3 if j == 0 else row[j] for j in range(len(row))] for row in matrix]

print("\nРезультат (первый столбец возведён в куб):")
for row in matrix_cubed:
    print(row)
print("Программа успешно выполнена!")