"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
# у словаря сложность по о-нотации ниже, при малых значениях это не сильно видно
# но как только запихнуть по больше значений, разница сразу ощутима. Удаление элементов, сколько раз не
# менял значение, одинаково :\

import time
from random import randint

docket = []
vocabulary = {}


def get_time(func):
    def wrapper(*args, **kwargs):
        time.process_time()
        result = func(*args, **kwargs)
        print(func.__name__, time.process_time())
        return result

    return wrapper


@get_time  # O(n)
def docket_in():
    for i in range(randint(0, 10000000)):  # O(n)
        docket.append(randint(0, 250))  # O(1)


@get_time  # O(n)
def vocabulary_in():
    for i in range(10000000):  # O(n)
        vocabulary[i] = chr(randint(20, 50))  # O(1)


@get_time  # O(n)
def pop_docket():
    docket.pop()


@get_time  # O(1)
def pop_vocabulary():
    vocabulary.pop(1)


@get_time  # O(n log n)
def sort_docket():
    docket.sort()


@get_time  # O(1)
def clear_vocabulary():
    vocabulary.clear()


vocabulary_in()
docket_in()

pop_vocabulary()
pop_docket()
sort_docket()
clear_vocabulary()
