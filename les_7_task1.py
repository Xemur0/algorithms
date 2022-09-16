"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit

orig_lst = [randint(-100, 100) for x in range(100)]
print(orig_lst)


def bubble_1(lst_obj):
    a = 0

    while a < len(lst_obj):
        for i in range(len(lst_obj) - 1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        a += 1
    return lst_obj


def bubble_2(lst_obj):
    a = 0

    while a < len(lst_obj):
        check = 1
        for i in range(len(lst_obj) - a - 1):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                check = 0
        if check == 1:
            break
        a += 1
    return lst_obj


print(timeit('bubble_1(orig_lst[:])', globals=globals(), number=10000))
print(timeit('bubble_2(orig_lst[:])', globals=globals(), number=10000))

#После того как элемент ставится в конец, прерывание
#тем самым выигрываем драгоценное времечко
