# 04-zp

## Описание
Этот код предназначен для генерации двоичных кодов заданной длины, которые не являются префиксами или не имеют префиксов среди существующих кодов. Это полезно в контексте кодирования символов, где мы хотим избежать неоднозначности при декодировании.

## Код
```python
# Функция для генерации всех возможных двоичных строк заданной длины,
# которые не являются префиксами или не имеют префиксов среди existing_codes
def get_fano_codes(existing_codes, length):
    return [bin(i)[2:].zfill(length) for i in range(2**length) 
            if not any(r.startswith(w) or w.startswith(r) for w in existing_codes for r in [bin(i)[2:].zfill(length)])]

# Исходные буквы и их двоичные представления
letters = 'АБВГ'
initial_mapping = {'А':'000', 'Б':'1', 'В': '011'}
binary_representations = list(initial_mapping.values())

i = 1 #Опционально взависимости от задачи, !В основном i = 1; или i = len(lis) + 1;

# Генерация новых двоичных представлений, которые не являются префиксами существующих
while len(binary_representations)<len(letters): 
    if len(letters)-len(binary_representations) == 1:
        new_binary_strings = get_fano_codes(binary_representations, i - 1)
        if new_binary_strings:
            binary_representations.append(new_binary_strings[0])
            break
    new_binary_strings = get_fano_codes(binary_representations, i)
    if new_binary_strings:
        binary_representations.append(new_binary_strings[0])
    i += 1

# Добавление новых букв и их двоичных представлений в словарь
new_binary_representations = sorted(set(binary_representations) - set(initial_mapping.values()), key=len)
initial_mapping.update(zip(set(letters) - set(initial_mapping.keys()), new_binary_representations))

print(binary_representations)
print(initial_mapping)
print(f'Anwser: {sum(len(code) for code in initial_mapping.values())}')
```
## Объяснение
- `get_fano_codes(existing_codes, length)` - это функция, которая генерирует все возможные двоичные строки заданной длины, которые не являются префиксами или не имеют префиксов среди `existing_codes`.
- `letters` - это строка символов, для которых мы хотим сгенерировать двоичные коды.
- `initial_mapping` - это словарь, который содержит начальное отображение символов на двоичные коды.
- `binary_representations` - это список текущих двоичных кодов.
- В цикле `while`, мы генерируем новые двоичные коды, которые не являются префиксами существующих кодов, пока количество текущих двоичных кодов не станет равным количеству символов.
- Затем мы добавляем новые буквы и их двоичные представления в словарь `initial_mapping`.
- В конце мы выводим список всех двоичных представлений, окончательное отображение и сумму длин всех кодов. Это может быть полезно для проверки эффективности кодирования.
