# Домашнее задание к лекции 4.Коллекции данных.Словари.Множества»

Перед выполнением задания прочитайте короткую статью [про типы данных](https://wombat.org.ua/AByteOfPython/data_structures.html) и отличную [статью на Хабре](https://habr.com/ru/post/319164/)

## Задание 1  
Дан список с визитами по городам и странам.  Напишите код, который возвращает отфильтрованный список geo_logs, содержащий только визиты из России."
```python
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]
```

## Задание 2  
Выведите на экран все уникальные гео-ID из значений словаря ids.   
Т.е. список вида [213, 15, 54, 119, 98, 35]
```python
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
``` 

## Задание 3  
Дан список поисковых запросов. Получить распределение количества слов в них.
Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
```python
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
```

## Задание 4  
Дана статистика рекламных каналов по объемам продаж.  
Напишите скрипт, который возвращает название канала с максимальным объемом.  
Т.е. в данном примере скрипт должен возвращать 'yandex'.  
```python
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
```

## Задание 5(Необязательное)  
Напишите код для преобразования произвольного списка вида ```['2018-01-01', 'yandex', 'cpc', 100]``` (он может быть любой длины) в словарь
```{'2018-01-01': {'yandex': {'cpc': 100}}}```



Для подготовки к следующей лекции прочитайте про [функции](https://foxford.ru/wiki/informatika/funktsii-v-python)

---
## Материал по теме. 
Рекомендованные статьи на русском языке:
1. [Осваиваем Python. Унция 1. Типы данных.](https://habr.com/ru/articles/49671/)
2. [Типы данных в Python.](https://pythonworld.ru/tipy-dannyx-v-python)
3. [Типы данных в Python.](http://pythonicway.com/python-data-types)
4. [Python с нуля. Часть 2. Типы переменных.](https://rtfm.co.ua/books-translations/python_s_nulya/python-s-nulya-chast-2-tipy-peremennyx/)
5. [Структуры данных.](https://wombat.org.ua/AByteOfPython/data_structures.html)

Рекомендованные статьи на английском языке:
1. [Python - Variable Types.](https://www.tutorialspoint.com/python/python_variable_types.htm)
2. [Variables and Types.](https://www.learnpython.org/en/Variables_and_Types)
3. [Learn X in Y minutes.](https://learnxinyminutes.com/docs/python/)
4. [Control Flow.](https://python.swaroopch.com/control_flow.html)
5. [PyFormat.](https://pyformat.info/)

Официальная документация:
1. [Built-in Types.](https://docs.python.org/3/library/stdtypes.html)
2. [Input and Output.](https://docs.python.org/3/tutorial/inputoutput.html)