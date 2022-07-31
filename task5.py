# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

import random

list_of_nums = [random.randint(1,11) for i in range (5)]
print (list_of_nums)

def find_mult_of_pairs(some_list):
    result_list = []
    first_index = 0
    last_index = len(some_list) - 1

    while last_index - first_index >= 0:
        result_list.append(some_list[first_index] * some_list[last_index])
        first_index = first_index + 1
        last_index = last_index -1
    return(result_list)

mult = find_mult_of_pairs(list_of_nums)
print (mult)