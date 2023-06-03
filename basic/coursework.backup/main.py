# -*- coding: utf-8 -*-

import os
from time import sleep
from token_manager import Token
from vk_api import vk_client
from yandex_api import yandex_client
from google_api import google_client


class Menu():
    def __init__(self):
        self.width = 80 
        self.sep = "#"*(self.width+2)
        self.menu = 0
        self.service = None
        self.selector()
    
    def header(self) -> None:
        text_1 = 'backup O.VER.9000'
        os.system("cls")
        print(
            self.sep, 
            f'{text_1}{(self.width-len(text_1))*" "}#',
            sep="#\n# "
            )

    def ask(self, item_name: str) -> str:
        text_1 = 'Для продолжения введите {}!'.format(item_name)
        print(
            self.sep, 
            f'{text_1}{(self.width-len(text_1))*" "}#', 
            sep="#\n# "
            )
        item = input(self.sep + "#\n" + "Ввод: ")
        return item

    def progress_bar(self, counter: int, max_count: int) -> None:
        progress = counter * int(self.width / max_count)
        if progress >= 80:
            progress = 79
        text_1 = '\\' * (progress)
        print(
            self.sep, 
            f' {text_1}{(self.width-len(text_1))*" "}',
            self.sep,
            sep="#\n#"
        )

    def privat_profile_error(self):
        text_1 = 'Профиль {} закрыт, операция недоступна!'.format(vk_client.profile_name)
        print(
            self.sep, 
            f'{text_1}{(self.width-len(text_1))*" "}#',
            sep="#\n# "
            )
        print(self.sep + '#')

    def change_operation(self, operation: int) -> None:
        if operation in range(1, 3):
            if operation == 1:
                album_id = 'profile'
            elif operation == 2:
                album_id = 'wall'   

            data = vk_client.get_photos(vk_client.profile_id ,album_id)
            keys = data.keys()
            counter = 1
            max_count = len(keys)

            if self.service == 1:
                try:
                    if yandex_client.get_folder(vk_client.profile_name) == False:
                        yandex_client.create_folder(vk_client.profile_name)
                        
                    for key in keys:
                        href = yandex_client.get_upload_link(vk_client.profile_name, key).get("href", "")
                        yandex_client.upload_file_to_disk(href, data[key])
                        self.header()
                        self.progress_bar(counter, max_count)
                        counter += 1

                except KeyError:
                    self.header()
                    self.privat_profile_error()

            elif self.service == 2:
                try:
                    if google_client.get_folder(vk_client.profile_name) == None:
                        google_client.create_folder(vk_client.profile_name)
                    folder_id = google_client.get_folder(vk_client.profile_name)

                    for key in keys:
                        google_client.upload_file_to_drive(data[key], key, folder_id)
                        self.header()
                        self.progress_bar(counter, max_count)
                        counter += 1

                except KeyError:
                    self.header()
                    self.privat_profile_error()

            sleep(3)

    def selector(self) -> None:
        while True:
            self.header()

            if self.menu == 0:
                user_id = self.ask('id пользователя vk')
                user_info = vk_client.get_user_info(user_id)
                try:
                    vk_client.profile_id = user_info['response'][0]['id']
                except IndexError:
                    continue
                vk_client.profile_name = '{} {}'.format(user_info['response'][0]['first_name'], user_info['response'][0]['last_name'])
                self.menu += 1

            elif self.menu == 1:
                button_1 = '1. Резервное копирование на Яндекс диск'
                button_2 = '2. Резервное копирование на Google Drive'
                button_3 = '3. Сменить целевого пользователя "Вконтакте" ({})'.format(vk_client.profile_name)
                button_4 = '4. Выход'
                print(
                    self.sep, 
                    f'{button_1}{(self.width-len(button_1))*" "}',
                    f'{button_2}{(self.width-len(button_2))*" "}', 
                    f'{button_3}{(self.width-len(button_3))*" "}',
                    f'{button_4}{(self.width-len(button_4))*" "}#',
                    sep="#\n# "
                    )
                answer = input(self.sep + "#\n" + "Ввод: ")

                if answer == "1":
                    self.service = 1     

                elif answer == "2":
                    self.service = 2

                elif answer == "3":
                    self.menu -= 1
                    continue

                elif answer == "4":
                    os.system("cls")
                    break

                else:
                    continue

                self.menu += 1

            elif self.menu == 2:
                if self.service == 1:
                    token_name, token = yandex_client.authentication()

                    if token is None:
                        token = self.ask(token_name)
                        Token().write_token(token_name, token)

                    else:
                        try:
                            yandex_account_info = yandex_client.get_account_info()
                            yandex_client.profile_name = '{}'.format(yandex_account_info['user']['display_name'])
                            self.menu += 1

                        except KeyError:
                            token = self.ask(token_name)
                            Token().write_token(token_name, token)

                elif self.service == 2:
                    token_name, token = google_client.authentication()

                    if token is None:
                        token = self.ask(token_name)
                        Token().write_token(token_name, token)

                    else:
                        try:
                            google_account_info = google_client.get_account_info()
                            google_client.profile_name = '{}'.format(google_account_info['user']['displayName'])
                            self.menu += 1

                        except KeyError:
                            token = self.ask(token_name)
                            Token().write_token(token_name, token)

            elif self.menu == 3:
                if self.service == 1:
                    service = 'Яндекс диск'
                    profile_name = yandex_client.profile_name
                elif self.service == 2:
                    service = 'Google Drive'
                    profile_name = google_client.profile_name
                button_1 = '1. Скачать фото профиля'
                button_2 = '2. Скачать фото со стены'
                button_3 = '3. Изменить лимиты (макс. {} изображений за операцию)'.format(vk_client.default_count_pictures)
                button_4 = '4. Сменить учётную запись "{}" ({})'.format(service, profile_name)
                button_5 = '5. Назад'
                print(
                    self.sep, 
                    f'{button_1}{(self.width-len(button_1))*" "}', 
                    f'{button_2}{(self.width-len(button_2))*" "}', 
                    f'{button_3}{(self.width-len(button_3))*" "}', 
                    f'{button_4}{(self.width-len(button_4))*" "}', 
                    f'{button_5}{(self.width-len(button_5))*" "}#',
                    sep="#\n# ")
                answer = input(self.sep + "#\n" + "Ввод: ")

                if answer == "1":
                    self.change_operation(1)

                elif answer == "2":
                    self.change_operation(2)

                elif answer == "3":
                    self.header()
                    count = self.ask('кол-во')
                    vk_client.default_count_pictures = int(count)

                elif answer == "4":
                    if self.service == 1:
                        token_name, token = yandex_client.authentication()
                    elif self.service == 2:
                        token_name, token = google_client.authentication()
                    self.header()
                    token = self.ask(token_name)
                    Token().write_token(token_name, token)
                    self.menu -= 1
                    continue

                elif answer == "5":
                    self.menu -= 2
                    continue

                else:
                    continue
            

if __name__ == "__main__":
    app = Menu()