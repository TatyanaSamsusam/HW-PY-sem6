# 2- Найти сумму чисел списка стоящих на нечетной позиции
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

list_of_nums = [random.randint(1,11) for i in range (5)]
print (list_of_nums)

list_of_nums = list(filter(lambda elem: list_of_nums.index(elem)%2, list_of_nums))
print(sum(list_of_nums))
