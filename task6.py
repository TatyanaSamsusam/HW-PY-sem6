# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def get_sequence(n):
    return [-3 **i for i in range(1, n+1)]
answer = get_sequence(5)
print(answer)

