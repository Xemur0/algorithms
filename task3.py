"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...
Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.
[5, 3, 4, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 4, 5]
my_lst
new_lts
arr[m]
from statistics import median
[3, 4, 3, 3, 5, 3, 3]
left = []
right = []
left == right and
for i in
    for
    left == right
    left.clear()
    right.clear()
"""
import numpy
from statistics import median
import timeit


def gnome(lst):
    i, size = 1, len(lst)
    while i < size:
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i - 1], lst[i] = lst[i], lst[i - 1]
            if i > 1:
                i -= 1
    return lst


def get_med(lst):
    [lst.remove(max(lst)) for _ in range(len(lst) // 2)]
    return max(lst)


a = int(input('a: '))
arr = numpy.random.randint(0, 100, 2 * a + 1)
print(arr)
print(f'statistics = {median(arr)}')
arr2 = gnome(arr.tolist())
print(f'gnome = {arr2[a]}')
print(f'without sort = {get_med(arr.tolist())}')
print(f'gnome: {timeit.timeit("gnome(arr[:])", globals=globals(), number=10000)}')
print(f'without sort: {timeit.timeit("get_med(arr[:].tolist())", globals=globals(), number=10000)}')

#Медиана находится быстрее сортировкой
#Гномья не самая быстрая, тем более с большим обьемом входящих данных
#хорошо конечно изобретать велосипед, но встроенные функции всегда хороши