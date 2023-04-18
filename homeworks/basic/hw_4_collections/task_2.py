# -*- coding: utf-8 -*-


ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def custom_filter(ids_list: str) -> list:

    result = []

    for key in ids.keys():
        for id in ids.get(key):
            if id not in result:
                result.append(id)

    return result