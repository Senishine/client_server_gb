""" 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе."""

word_1 = b'attribute'
print(word_1)

# word_2 = b'класс' # нельзя записать в байтовом типе, будет ошибка "bytes can only contain ASCII literal characters"
word_2 = 'класс'.encode('utf-8')
print(word_2)

# word_3 = b'функция' # нельзя записать в байтовом типе, будет ошибка "bytes can only contain ASCII literal characters"
word_3 = 'функция'.encode('utf-8')
print(word_3)

word_4 = b'type'
print(word_4)
