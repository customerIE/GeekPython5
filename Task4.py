# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#
with open('Data_input.txt', 'r') as file:
    line = file.readline()
    list_line = line.split()

print(f'Исходная строка -       {line}')

# Кодирование данных
def coding(txt):
    encond = ''
    prev_char = ''
    count = 1
    if not txt:
        return ''

    for char in txt:
        if char != prev_char:
            if prev_char:
                encond += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encond += str(count) + prev_char
        return encond


list_line = coding(line)

with open('Data_encoding.txt', 'w', encoding='UTF-8') as file:
    file.write(f'{list_line}')
print(f'Кодированная строка -   {list_line}')

# Восстановление данных
with open('Data_encoding.txt', 'r') as file1:
    line1 = file1.readline()
    list_line1 = line1.split()

def decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = ''
    return decode

list_line1 = decode(line1)
with open('Data_output.txt', 'w', encoding='UTF-8') as file2:
    file2.write(f'{list_line1}')
print(f'Декодированная строка - {list_line1}')
 
