# 1- Определить, присутствует ли в заданном списке строк, некоторое число


mama_list = ['мама', 'сшила', 'м0не', 'штаны', 'и7з', 'бере9зовой', 'кор45ы']
print(' '.join(list(filter(lambda word: not any (char.isdigit() for char in word), mama_list))))