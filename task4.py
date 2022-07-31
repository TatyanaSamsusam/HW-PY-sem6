# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


my_list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
word_to_find = "qwe"

def second_coming (some_list, str):
    return[i for i, element in enumerate(some_list) if str in element][1]if len(some_list) > 2 else 0
answer = second_coming(my_list, word_to_find)
print(answer)