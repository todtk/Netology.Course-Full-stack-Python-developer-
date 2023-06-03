# -*- coding: utf-8 -*-

import requests, json
from token_manager import Token


class Google_Api():
    def __init__(self):
        self.token_name = 'google.token'
        self.profile_name = 'Не авторизован'
        self.headers = {
            'Content-type': 'application/json',
        }

    def authentication(self) -> None:
        token = Token().read_token('google.token')
        self.headers['Authorization'] = 'Bearer {}'.format(token)
        return self.token_name, token

    def get_account_info(self) -> dict:
        url = 'https://www.googleapis.com/drive/v3/about'
        params = {
            'fields': 'user'
        }
        response = requests.get(url, headers=self.headers, params=params).json()
        return response

    def get_folder(self, folder_name: str) -> str:
        url = 'https://www.googleapis.com/drive/v3/files'
        params = {
            'q': "mimeType = 'application/vnd.google-apps.folder'"
        }
        response = requests.get(url, headers=self.headers, params=params).json()
        for file in response['files']:
            if file['name'] == folder_name:
                return file['id']
            else:
                return None

    def create_folder(self, folder_name: str) -> None:
        url = 'https://www.googleapis.com/drive/v3/files' 
        metadata = {
            'mimeType': 'application/vnd.google-apps.folder',
            'name': folder_name
        }
        requests.post(url, headers=self.headers, data=json.dumps(metadata))

    def upload_file_to_drive(self, img_url: str, file_name: str, folder_id: str) -> None:
        url = 'https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart'
        headers = {
            'Authorization': self.headers['Authorization'],
        }
        metadata = {
            'name': '{}.jpg'.format(file_name),
            'parents': [folder_id]
        }
        files = {
            "data": (
                "metadata",
                json.dumps(metadata),
                "application/json; charset=UTF-8"
                ),
            "file": requests.get(img_url).content
            }
        requests.post(url, headers=headers, files=files)


google_client = Google_Api()