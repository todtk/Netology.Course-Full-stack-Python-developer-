# -*- coding: utf-8 -*-

import requests
from token_manager import Token


class Yandex_Api():
    def __init__(self):
        self.token_name = 'yandex.token'
        self.profile_name = 'Не авторизован'
        self.headers = {
            'content-type': 'application/json', 
        }

    def authentication(self) -> str:
        token = Token().read_token(self.token_name)
        self.headers['Authorization'] = 'OAuth {}'.format(token)
        return self.token_name, token

    def get_account_info(self) -> dict:
        url = "https://cloud-api.yandex.net/v1/disk"
        params = {
            'fields': 'user'
        }
        response = requests.get(url, headers=self.headers, params=params).json()
        return response

    def get_folder(self, folder_name: str) -> bool:
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {
            'path': '{}'.format(folder_name)
        }
        response = requests.get(url, headers=self.headers, params=params).json()

        if response.get('message') == "Не удалось найти запрошенный ресурс.":
            return False
        else:
            return True

    def create_folder(self, folder_name: str) -> None:
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        params = {
            'path': folder_name
        }
        requests.put(url, headers=self.headers, params=params)

    def get_upload_link(self, folder_name: str, file_name: str) -> dict:
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {
            "path": '{}/{}.jpg'.format(folder_name, file_name), 
            "overwrite": "true"
            }
        response = requests.get(url, headers=self.headers, params=params).json()
        return response

    def upload_file_to_disk(self, href: str, img_url: str) -> None:
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        bytearray = requests.get(img_url).content
        requests.put(href, bytearray)


yandex_client = Yandex_Api()