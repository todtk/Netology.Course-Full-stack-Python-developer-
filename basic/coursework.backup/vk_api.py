# -*- coding: utf-8 -*-

import requests, os, json
from datetime import datetime


class VK_api():
    def __init__(self):
        self.default_count_pictures = 5
        self.headers = {
            'v': '5.131',
            'access_token': 'f77b4472f77b4472f77b447271f46b3847ff77bf77b447294706a52d2ec565f42c96162'
        }

    def authentication(self) -> str:
        return None, self.headers['access_token']

    def get_user_info(self, display_name) -> dict:
        url = 'https://api.vk.com/method/users.get'
        params = {
            'user_ids': display_name
        }
        response = requests.get(url, params={**self.headers, **params}).json()
        return response

    def name_controller(self, owner_id: int, item: dict) -> str:
        name = item['likes']['count']
        date = datetime.utcfromtimestamp(item['date']).strftime('%Y-%m-%d')
        size = item['sizes'][-1]['type']

        base_path = os.getcwd()
        json_path = 'json'
        file_path = '{}.json'.format(owner_id)
        path = os.path.join(base_path, json_path, file_path)
        try:
            os.mkdir(os.path.join(base_path, json_path))
        except FileExistsError:
            pass
        if os.path.exists(path):
            with open(path, 'r') as json_file:
                json_data = json.load(json_file)

            for item in json_data:
                if item.get('file_name') == name:
                    name = '{}_{}'.format(name, date)

            new_file = {
                'file_name': name,
                'size': size
            }

            json_data.append(new_file)
            with open(path, 'w') as json_file:
                json.dump(json_data, json_file)

        else:
            json_data = [{
                'file_name': name,
                'size': size
            }]

            with open(path, 'w') as json_file:
                json.dump(json_data, json_file)
        
        return name

    def get_photos(self, owner_id: int, album_id: str) -> dict:
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'extended': 1,
            'owner_id': owner_id,
            'album_id': album_id,
            'count': self.default_count_pictures
        }
        response = requests.get(url, params={**self.headers, **params}).json()

        data = {}
        counter = 1
        for item in response['response']['items']:
            name = str(item['likes']['count'])
            name = self.name_controller(owner_id, item)
            url = item['sizes'][-1]['url']
            data[name] = url
            counter += 1
        
        return data


vk_client = VK_api()