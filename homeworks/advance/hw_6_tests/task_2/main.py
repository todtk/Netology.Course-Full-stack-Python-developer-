# -*- coding: utf-8 -*-

import os, pathlib, requests


class YandexAPI():
    def __init__(self):
        self.headers = {
            'content-type': 'application/json', 
        }

    @staticmethod
    def get_token() -> str:
        
        pathlib.Path(os.path.join(os.getcwd(), "tokens")).mkdir(parents=True, exist_ok=True)
        path = os.path.join(os.getcwd(), "tokens", "yandex.token")

        if os.path.exists(path):
            with open(path, encoding="utf-8") as token_file:
                return token_file.read()
        else:
            token = input("Введите токен: ")
            with open(path, "w", encoding="utf-8") as token_file:
                token_file.write(token)
                return token

    def get_auth(self) -> None:

        token = self.get_token()
        self.headers['Authorization'] = 'OAuth {}'.format(token)

    def create_folder(self, name: str) -> requests.Response:

        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': name}

        return requests.put(url, headers=self.headers, params=params)