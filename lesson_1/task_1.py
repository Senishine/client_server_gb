""" Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание
соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и
также проверить тип и содержимое переменных."""

word_str = 'разработка'
print(word_str)
print(type(word_str))
word_to_bytes = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
print(type(word_to_bytes))
word_2_str = 'сокет'
print(word_2_str)
print(type(word_2_str))
word_2_to_bytes = '\u0441\u043e\u043a\u0435\u0442'
print(type(word_2_to_bytes))
word_3_str = 'декоратор'
print(word_3_str)
print(type(word_3_str))
word_3_to_bytes = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
print(type(word_3_to_bytes))




