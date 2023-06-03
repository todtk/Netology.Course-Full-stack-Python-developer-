# -*- coding: utf-8 -*-


queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]


def words_counter(queries : list) -> dict:
    
    counter = {}

    for querie in queries:
        querie_splited = querie.split(" ")

        count_words = len(querie_splited)

        if counter.get(count_words) is None:
            counter[count_words] = 1
        else:
            counter[count_words] = counter[count_words] + 1

    return counter

def persent_counter(words_counter : dict) -> dict:

    persents = {}

    max_count = sum(words_counter.values())

    for counter in words_counter.keys():
        persents[counter] = (100 / max_count) * words_counter[counter]

    return persents