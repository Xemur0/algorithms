"""
Задание 1.
Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.
Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов
Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import memory_profiler
from timeit import default_timer
from pympler import asizeof


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        print(f'memory: {m2[0] - m1[0]}, time: {default_timer() - start_time}')
        return res
    return wrapper


# 1
class Car:
    __slots__ = ('speed', 'color', 'name', 'is_police')

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.ispolice = is_police

    @decor
    def go(self):
        return f'{self.name} {self.color} Погнала'

    @decor
    def stop(self):
        return f'{self.name} {self.color} Остановилась'

    @decor
    def turn(self, direction):
        return f'{self.name} {self.color} Повернула {direction}'

    @decor
    def show_speed(self):
        return f'Скорость {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)

    @decor
    def show_speed(self):
        if self.speed > 60:
            return f'Нарушил скоростной режим {self.speed}'
        else:
            return f'Скорость {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=False)

    @decor
    def show_speed(self):
        if self.speed > 40:
            return f'Нарушил скоростной режим - текущая скорость {self.speed}'
        else:
            return f'Скорость {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)


a = WorkCar(50, 'черная', 'Mazda')  # до применения слотов, 344. После применения, 264
b = PoliceCar(120, 'белая', 'Lada')  # до 336, после 256
c = SportCar(120, 'зеленая', 'Honda')  # до 344, после 264
print(asizeof.asizeof(a))
print(asizeof.asizeof(b))
print(asizeof.asizeof(c))

print(a.show_speed()) #memory: 0.00390625, time: 0.10812139999999998 Нарушил скоростной режим - текущая скорость 50
print(b.show_speed()) #memory: 0.0, time: 0.10803619999999997 Скорость 120
print(c.show_speed()) #memory: 0.0, time: 0.10759769999999991 Скорость 120

print(a.go()) #memory: 0.0, time: 0.10669899999999999 Mazda черная Погнала
print(b.go()) #memory: 0.0, time: 0.10757650000000019 Lada белая Погнала
print(c.go()) #memory: 0.0, time: 0.10732520000000001 Honda зеленая Погнала

print(a.stop()) #memory: 0.0, time: 0.10800739999999998 Mazda черная Остановилась
print(b.stop()) #memory: 0.0, time: 0.10762310000000008 Lada белая Остановилась
print(c.stop()) #memory: 0.0, time: 0.10771509999999984 Honda зеленая Остановилась


#применяем слоты
#a = WorkCar(50, 'черная', 'Mazda')  # до применения слотов, 344. После применения, 264
#b = PoliceCar(120, 'белая', 'Lada')  # до 336, после 256
#c = SportCar(120, 'зеленая', 'Honda')  # до 344, после 264

# memory: 0.00390625, time: 0.10716780000000004
# Нарушил скоростной режим - текущая скорость 50
# memory: 0.0, time: 0.10780779999999995
# Скорость 120
# memory: 0.0, time: 0.10762289999999997
# Скорость 120
# memory: 0.0, time: 0.10755800000000004
# Mazda черная Погнала
# memory: 0.0, time: 0.10753119999999994
# Lada белая Погнала
# memory: 0.0, time: 0.10740599999999989
# Honda зеленая Погнала
# memory: 0.0, time: 0.10812700000000008
# Mazda черная Остановилась
# memory: 0.0, time: 0.10788059999999988
# Lada белая Остановилась
# memory: 0.0, time: 0.10783639999999983
# Honda зеленая Остановилась
#

#так как особо тут ничего нет в функциях, разница еле ощутима, но зато создавая новые  обьекты, точно видна разница
#по количеству занимаемой памяти
#так как профайлер, все время указывал 0.0 MiB, написал декоратор. Доустановил Pympler для более точных отображений
#обьема обьектов

#2
#взят код из этого курса из 4ого урока
#на маленький числах, разница почти не видна, при значениях в районе 1000000, сразу видно, оптимизированный
#вариант с использованием генератора, ощутимо лучше, что по памяти, что по скорости
#ибо генератор опусташается, не храня массив

import memory_profiler
from timeit import default_timer


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        print(f'memory: {m2[0] - m1[0]}, time: {default_timer() - start_time}')
        return res

    return wrapper
@decor
def func_1(nums):

    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

func_1([i for i in range(0, 1000000)])

@decor
def func_new(nums):
    for index in range(len(nums)):
        if nums[index] % 2 == 0:
            yield index
        else:
            continue

func_new([i for i in range(0, 1000000)])





#3
# по заданию из основ питона, надо было вывести сумму всех нечетных чисел от 0 до 1000(условно)


@decor
def coub_lst(a):
    kub_list = []
    summary_list = 0
    for i in range(1, a, 2):
        kub_list.append(i ** 3)

    for i in kub_list:
        num = i
        s_num = 0
        while i > 0:
            digit = i % 10
            s_num = s_num + digit
            i = i // 10

        if s_num % 7 == 0:
            summary_list += num
    print(summary_list)

coub_lst(1000)


def nums_generator(max_num):
    for i in range(1, max_num + 1, 2):
        num = i ** 3
        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num //= 10
        yield i ** 3 if sum_num % 7 == 0 else 0


@decor
def coub_upgrade(n):
    nums_gen = nums_generator(n)
    full_summ = 0

    for _ in range(1, n + 1, 2):
        num = next(nums_gen)
        full_summ += num
    print(full_summ)

coub_upgrade(1000)

#пишем новую функция используя генератор, как раз он не хранит в памяти ничего, сразу же опусташаясь
#по памяти стало 0.0, по времени выйгрышь маленький, но он все равно есть


