""" Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
    программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
    Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
import locale

print(f'Кодировка {locale.getpreferredencoding()}')

fill_file = [
    'сетевое программирование',
    'сокет',
    'декоратор'
]

with open('test_file.txt', 'w', encoding='utf-8') as test_file:
    for string in fill_file:
        test_file.write(string + '\n')
    print(f'Кодировка файла "{test_file.name}" по умолчанию: {test_file.encoding}')

with open("test_file.txt", encoding='utf-8') as file:
    for line in file:
        print(line, end='')



