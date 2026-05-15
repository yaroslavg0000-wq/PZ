temperatures = [-2, -1, 0, 3, 5, 7, 8, 6, 4, 1, -1, -3, -5, -4, 0,
                2, 4, 6, 8, 0, 9, 7, 5, 3, 1, -1, -2, -3, -1, 0, 2]

print(f"Исходные данные (31 день):\n{temperatures}\n")

positive_count = sum(1 for t in temperatures if t > 0)
negative_count = sum(1 for t in temperatures if t < 0)

print(f"Количество положительных температур: {positive_count}")
print(f"Количество отрицательных температур: {negative_count}")

min_temp = min(temperatures)
max_temp = max(temperatures)

print(f"Самая низкая температура: {min_temp}°C")
print(f"Самая высокая температура: {max_temp}°C")

avg_temp = sum(temperatures) / len(temperatures)

print(f"Среднемесячная температура: {avg_temp:.2f}°C")
print("Программа выполнена успешно")
