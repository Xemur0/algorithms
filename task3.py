"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run

num = 77748294784556


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


print(timeit('revers_1(num)', globals=globals()))
run('revers_1(num)')

print(timeit('revers_2(num)', globals=globals()))
run('revers_2(num)')

print(timeit('revers_3(num)', globals=globals()))
run('revers_3(num)')

print(timeit('revers_4(num)', globals=globals()))
run('revers_4(num)')

# 1ая функция, медленней всего, рекурсия создает экспоненциальную сложность
# 2ая функция с циклом, много вычислений
# 3яя функция со срезом, отрабатывает намного быстрее чем все остальные
# 4ая функция теряет свое драгоценное время изза джоина, чтобы все это дело соединить. Зато красиво выглядит
# Как показало небольшое количество практики, всегда надо, по возможности, пользоваться встроенными функциями, делая
# при этом меньше телодвижений
