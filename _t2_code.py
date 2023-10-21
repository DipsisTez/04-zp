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
