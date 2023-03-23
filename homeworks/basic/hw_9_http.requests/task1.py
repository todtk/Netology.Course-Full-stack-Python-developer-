# -*- coding: utf-8 -*-

import requests
import json


def request_to_api() -> list:
    """ОБРАЩЕНИЕ К API, ПОЛУЧЕНИЕ СПИСКА ГЕРОЕВ С ИХ ПАРАМЕТРАМИ"""
    response = requests.get("https://akabab.github.io/superhero-api/api/all.json")
    response = json.loads(response.text)
    return response

def exract_data(response : list) -> dict:
    """ПОЛУЧАЕМ ИЗ RESPONSE НЕОБХОДИМЫЕ ДАННЫЕ, ФОРМИРУЕМ СЛОВАРЬ"""
    hero_dict = {}
    for item in response:
        name = item["name"]
        intelligence = item["powerstats"]["intelligence"]
        hero_dict[name] = intelligence
    return hero_dict

def find_intelligence(hero_dict : dict, selected_heroes : list) -> str:
    """ПОИСК И СОПОСТАВЛЕНИЕ ПО ПАРАМЕТРУ ИНТЕЛЕКТ"""
    result = None
    for hero in selected_heroes:
        intelligence = hero_dict[hero]
        if result is None:
            result = [hero, intelligence]
        else:
            if intelligence > result[1]:
                result = [hero, intelligence]
    return f"Cамый умный {result[0]}"


if __name__ == "__main__":
    response = request_to_api()
    hero_dict = exract_data(response)
    print(find_intelligence(hero_dict, ["Hulk", "Captain America", "Thanos"]))