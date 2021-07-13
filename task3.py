"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""



companies = {
    'apple' : 10900,
    'google' : 20000,
    'huawei' : 25000,
    'telefunken' : 5000,
    'ZTE' : 34534,
    'Meizu' : 555,
    'KFA2' : 23426,
    'Galax' : 6259,
    'Nvidia' : 3445,
    'AMD' : 76544,
    'Intel' : 65237,
    'MikroTik' : 25435
}

def find_companies(companies):
    sorted_values = sorted(companies.values(), reverse=True)  #O(1)
    sorted_dict = {}                        #O(1)
    for i in sorted_values:                 #O(n)
        for a in companies.keys():          #O(n) -> вложенный цикл, O(n^2)
            if companies[a] == i:
                sorted_dict[a] = companies[a]   #O(1)
                break
    count = 0                               #O(1)
    for i in sorted_dict.items():           #O(n)
        if count < 3:
            print(i)
        count += 1



print(find_companies(companies))

import itertools

from collections import Counter                 #наверно, можно считать константной. Придумывать велосипед, это конечно хорошо
                                                #работают мозги и все в таком духе, но уже до нас написано куча
                                                #библиотек, которыми можно пользоваться, как  например эта. В этом
                                                #плюс питона, импортируй -> влавствуй -> унижай xD

                                                #Вывод: если ты не преисполнился в своем сознании и не можешь
                                                #сообразить новый алгоритм, используй ранее оптимизорованными
                                                #библиотеками
print(dict(Counter(companies).most_common(3)))


                #Дмитрий, я знаю что получу заглушку, из-за работы, не успел все доделать
                #как только доделаю, пришлю по форме Вам сообщение о выполненой работе, чтобы получить
                # более наивысшую оценку:)