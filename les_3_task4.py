"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если есть, получаем
если нет, то вносить ее в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

import hashlib

tr_cache = {}


def get_cache(arr):
    salt = 'salam'
    hash_obj = hashlib.sha256(arr.encode() + salt.encode()).hexdigest()
    x = tr_cache.get(hash_obj)
    if not x:
        tr_cache[hash_obj] = arr
        print('Added to hash table')
    else:
        print('Find in hash table')


get_cache('https://vk.com/feed')
get_cache('https://vk.com/feed')
get_cache('https://vk.com/feed')
