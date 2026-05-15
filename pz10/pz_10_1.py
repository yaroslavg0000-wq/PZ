with open('numbers_6.txt', 'w') as f:
    f.write('-3 7 7 2 -5 8 8 8 10 -1 3 3')

with open('numbers_6.txt', 'r') as f:
    numbers = list(map(int, f.read().split()))

product = 1
for num in numbers:
    product *= num

duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

increased = []
for num in numbers:
    if num > 5:
        increased.append(num * 2)

with open('result_6.txt', 'w') as f:
    f.write('Исходные данные:\n')
    f.write(' '.join(map(str, numbers)) + '\n')
    f.write(f'Количество элементов: {len(numbers)}\n')
    f.write(f'Произведение элементов: {product}\n')
    f.write(f'Повторяющиеся элементы: {duplicates}\n')
    f.write(f'Количество повторяющихся элементов: {len(duplicates)}\n')
    f.write(f'Элементы больше 5 увеличены в два раза: {increased}\n')

print("Готово! Результат в файле result_6.txt")
print("Программа выполнена успешно")