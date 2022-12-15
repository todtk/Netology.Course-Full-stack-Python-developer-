# -*- coding: utf-8 -*-

import os
import requests


class YandexDisk():
    
    def login_(self) -> str:
        """ПРОВЕРЯЕТ НАЛИЧИЕ ТОКЕНА, ЗАПРАШИВАЕТ И СОЗДАЁТ ПРИ НЕОБХОДИОМСТИ"""
        """ТОКЕН ВЫНЕСЕН ИЗ РЕПОЗИТОРИЯ В ПОЛЬЗОВАТЕЛЬСКОЕ ОКРУЖЕНИЕ"""
        token_path = f"C:/Users/{os.getlogin()}/.keys/yandex.token"
        if os.path.exists(token_path):
            with open(token_path, "r", encoding="utf-8") as token_file:
                token = token_file.read()
                return token
        if not os.path.exists(token_path):
            user_token = input("Введите ваш токен от Yandex disk: ")
            with open(token_path, "w", encoding="utf-8") as token_file:
                token_file.write(user_token)
                return user_token

    def get_headers(self) -> dict:
        return {
            "Content-Type": "application/json",
            "Authorization": "OAuth {}".format(self.login_())
        }

    def file_list(self) -> dict:
        """ПОЛУЧАЕМ СПИСОК ФАЙЛОВ"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/files"
        headers = self.get_headers()
        response = requests.get(url, headers=headers)
        os.system("cls")
        for item in response.json()["items"]:
            print("Имя: {}, {} байт".format(item["name"], item["size"]))
        input()

    def get_download_link(self):
        """ПОЛУЧАЕМ ССЫЛКУ НА СКАЧИВАНИЕ"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/download"
        headers = self.get_headers()
    
    def download_file_from_disk(self):
        """СКАЧИВАЕМ ФАЙЛ"""
        pass

    def get_upload_link(self, path_on_yandex_disk: str) -> dict:
        """ПОЛУЧАЕМ ССЫЛКУ НА ЗАГРУЗКУ"""
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": path_on_yandex_disk, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, path_on_the_computer: str, path_on_yandex_disk: str) -> None:
        """ЗАГРУЖАЕМ ФАЙЛ"""
        href = self.get_upload_link(path_on_yandex_disk).get("href", "")
        response = requests.put(href, data=open(path_on_the_computer, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            os.system("cls")
            print("Загрузка успешно завершена.")
            input()
        else:
            print("Ошибка.")


if __name__ == "__main__":
    disk = YandexDisk()
    while True:
        user_command = input("1. Список файлов\n2. Скачать файл\n3. Загрузить файл\n4. Удалить файл\n5. Netology script\n6. Выход\nВыберите номер действия: ")
        if int(user_command) == 1:
            disk.file_list()
        elif int(user_command) == 2:
            os.system("cls")
            print("В разработке, попробуйте позже!")
            input()
        elif int(user_command) == 3:
            path_on_the_computer = input("Укажите путь к файлу на вашем компьютере в формате C:\\users\\user\\desktop\\example.jpg : ")
            path_on_yandex_disk = input("Укажите путь и имя для загрузки на Яндекс диск в формате folder/example.jpg : ")
            disk.upload_file_to_disk(path_on_the_computer, path_on_yandex_disk)
        elif int(user_command) == 4:
            os.system("cls")
            print("В разработке, попробуйте позже!")
            input()
        elif int(user_command) == 5:
            path_on_the_computer = input("Укажите путь к файлу на вашем компьютере в формате C:\\users\\user\\desktop\\example.jpg : ")
            fragments = path_on_the_computer.split("\\")
            path_on_yandex_disk = fragments[-1]
            disk.upload_file_to_disk(path_on_the_computer, path_on_yandex_disk)
        elif int(user_command) == 6:
            os.system("cls")
            print("Работа программы завершена пользователем.")
            break
        else:
            print("Некорректный ввод.")
            input()
        os.system("cls")