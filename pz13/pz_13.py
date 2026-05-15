import re

with open('ip_address.txt', encoding='utf-8') as f:
    text = f.read()

section = re.search(r'Зарезервированные адреса.+', text, re.DOTALL).group()

lines = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?:/\d+)?\t.+', section)

non_zero = []
other = []

for line in lines:
    match = re.match(r'(\d+)\.(\d+)\.', line)
    if match and match.group(1) != '0' and match.group(2) != '0':
        non_zero.append(line)
    else:
        other.append(line)

with open('../non_zero_octets.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(non_zero))

with open('../other_octets.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(other))

print(f'Файл 1 (ненулевые 1-й и 2-й октеты): {len(non_zero)} строк')
print(f'Файл 2 (остальные): {len(other)} строк')
print("\nПрограмма выполнена успешно")