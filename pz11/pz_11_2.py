def to_lower_generator(text):
    for char in text:
        yield char.lower()


print("\n" + "=" * 50)
print("Генератор: перевод в нижний регистр")
print("=" * 50)

original_string = "PyThon ProGramming Is FUn!"
print(f"Исходная строка: {original_string}")

lower_generator = to_lower_generator(original_string)

result_string = ''.join(lower_generator)

print(f"Результат (нижний регистр): {result_string}")

print("\n--- Альтернативный вариант (списковое включение) ---")
alternative_result = ''.join(char.lower() for char in original_string)
print(f"Результат: {alternative_result}")
print("Программа выполнена успешно")