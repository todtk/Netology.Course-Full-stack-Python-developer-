# -*- coding: utf-8 -*-

from unittest import TestCase, expectedFailure
from main import YandexAPI


class TestYandexAPI(TestCase):

    @classmethod
    def setUpClass(self):
        self.ya = YandexAPI()
        self.ya.get_auth()
    
    def test_basic_create(self):
        
        response = self.ya.create_folder(name="test_folder")
        self.assertEqual(response.status_code, 201)

    @expectedFailure
    def test_folder_empty_name(self):

        response = self.ya.create_folder(name="")
        self.assertEqual(response.status_code, 201)