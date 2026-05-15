import random

rows = 4
cols = 5

original_matrix = [[random.randint(0, 20) for _ in range(cols)] for _ in range(rows)]

print("Сгенерированная исходная матрица:")
for row in original_matrix:
    print(row)

filtered_matrix = [[0 if element > 10 else element for element in row] for row in original_matrix]

print("\nМатрица после замены (элементы > 10 заменены на 0):")
for row in filtered_matrix:
    print(row)
print("Программа успешно выполнена!")