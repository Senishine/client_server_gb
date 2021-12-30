""" 4.Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode)."""

word_1 = 'разработка'
word_1_to_bytes = word_1.encode('utf-8')
word_1_to_str = word_1_to_bytes.decode('utf-8')
print(word_1_to_bytes, '\n', word_1_to_str)
word_2 = 'администрирование'
word_2_to_bytes = word_2.encode('utf-8')
word_2_to_str = word_2_to_bytes.decode('utf-8')
print(word_2_to_bytes, '\n', word_2_to_str)
word_3 = 'protocol'
word_3_to_bytes = word_3.encode('utf-8')
word_3_to_str = word_3_to_bytes.decode('utf-8')
print(word_3_to_bytes, '\n', word_3_to_str)
word_4 = 'standard'
word_4_to_bytes = word_4.encode('utf-8')
word_4_to_str = word_4_to_bytes.decode('utf-8')
print(word_4_to_bytes, '\n', word_4_to_str)

