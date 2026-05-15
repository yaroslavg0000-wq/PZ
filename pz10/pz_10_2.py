import string

try:
    with open('text18-6.txt', 'r', encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("Файл text18-6.txt не найден!")
    exit()

print("\nСодержимое файла text18-6.txt:")
print(content)

spaces_count = 0
for char in content:
    if char.isspace():
        spaces_count += 1

print(f"\nКоличество пробельных символов: {spaces_count}")

punctuation_marks = string.punctuation
new_content = content

for p in punctuation_marks:
    new_content = new_content.replace(p, '!')

with open('text18-6_new.txt', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nНовый файл 'text18-6_new.txt' создан!")
print("Знаки пунктуации заменены на '!'")

print("\nРезультат замены:")
print(new_content)
print("Программа выполнена успешно")