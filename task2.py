# 2- Найти сумму чисел списка стоящих на нечетной позиции
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

list_of_nums = [random.randint(1,11) for i in range (5)]
print (list_of_nums)

def find_sum_of_odd_elements (some_list):
    result = 0
    for i in range (1, len(some_list),2):
        result = result + some_list[i]
    return(result)

sum = find_sum_of_odd_elements(list_of_nums)
print (f'сумма элементов списка, стоящих на нечётной позиции, равна {sum}')