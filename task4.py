from collections import OrderedDict
from timeit import timeit


def load_dict():
    return {num: num ** 3 for num in range(1000)}


def load_ord_dict():
    return OrderedDict({num: num ** 3 for num in range(1000)})


my_dict = load_dict()
my_od = load_ord_dict()


def dict_get():
    return my_dict.get('200')


def order_get():
    return my_od.get('200')


print(f'Заполнение: {timeit("load_dict()", globals=globals(), number=10000)}')
print(f'Заполнение ord: {timeit("load_ord_dict()", globals=globals(), number=10000)}')
print(f'Получение: {timeit("dict_get()", globals=globals(), number=100000)}')
print(f'Получение ord: {timeit("order_get()", globals=globals(), number=100000)}')

# Стоит версия 3.8, ordereddict по заполнению оч проигрывает. По получению на моей машине разница особо не видна почему-то
#хотя вроде все верно сделал :D
