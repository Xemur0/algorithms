"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.
Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)
Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а
"""


def sub_string_generator(x=input('Enter word: ')):
    example_dict = {}
    for a in range(0, len(x) - 1):
        for b in range(a + 1, len(x) if a == 0 else len(x) + 1):
            sub_str = x[a: b]
            hs_sub_string = hash(sub_str)
            if hs_sub_string not in example_dict:
                example_dict[hs_sub_string] = sub_str
    print(f'Unique sub strings - {x}: {len(example_dict)}')
    for a in example_dict.values():
        print(a)


sub_string_generator()
