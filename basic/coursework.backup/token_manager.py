# -*- coding: utf-8 -*-

import os


class Token():
    def __init__(self):
        self.base_path = os.getcwd()
        self.catalog_name = ".keys"
        
    def read_token(self, token_name: str) -> str:
        token_path = os.path.join(self.base_path, self.catalog_name, token_name)
        if os.path.exists(token_path):
            with open(token_path, 'r') as file:
                token = file.read()
                return token
        else:
            return None

    def write_token(self, token_name: str, token: str) -> str:
        token_path = os.path.join(self.base_path, self.catalog_name, token_name)
        try:
            with open(token_path, 'w') as file:
                file.write(token)
        except FileNotFoundError:
            os.mkdir(os.path.join(self.base_path, self.catalog_name))
            with open(token_path, 'w') as file:
                file.write(token)
        return token

    def delete_token(self, token_name: str) -> None:
        token_path = os.path.join(self.base_path, self.catalog_name, token_name)
        os.remove(token_path)