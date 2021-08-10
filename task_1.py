"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

import heapq as hpq
from collections import defaultdict


def huffman_tree(freq):
    hp = [[weight, [char, '']] for char, weight in freq.items()]
    hpq.heapify(hp)
    while len(hp) > 1:
        left = hpq.heappop(hp)
        right = hpq.heappop(hp)
        for val in left[1:]:
            val[1] = '0' + val[1]
        for val in right[1:]:
            val[1] = '1' + val[1]
        hpq.heappush(hp, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(hpq.heappop(hp)[1:], key=lambda x: (len(x[-1]), x))


s_string = str(input('Введите строку для кодировки: '))

frequency = defaultdict(int)

for chars in s_string:
    frequency[chars] += 1

res_tree = huffman_tree(frequency)
print('Закодированная строка: ')
for _ in res_tree:
    print(_[1], end='')

