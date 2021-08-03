"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).
И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...
Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import operator
import timeit
import numpy


def merge_sort(lst, compare=operator.lt):
    if len(lst) < 2:
        return lst[:]
    else:
        middle = int(len(lst) / 2)
        left = merge_sort(lst[:middle], compare)
        right = merge_sort(lst[middle:], compare)
        return merge(left, right, compare)


def merge(left, right, compare):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


n = int(input('Введите количество элементов: '))
arr = numpy.random.uniform(0, 50, n)
print(arr)
print(merge_sort(arr))
arr = numpy.random.uniform(0, 50, 10)
print(f'10: {timeit.timeit("merge_sort(arr[:])", globals=globals(), number=1000)}')
arr = numpy.random.uniform(0, 50, 100)
print(f'100: {timeit.timeit("merge_sort(arr[:])", globals=globals(), number=1000)}')
arr = numpy.random.uniform(0, 50, 1000)
print(f'1000: {timeit.timeit("merge_sort(arr[:])", globals=globals(), number=1000)}')

#тут особо нечего сказать, слияние отрабатывает оч хорошо
