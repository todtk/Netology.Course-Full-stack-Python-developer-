# -*- coding: utf-8 -*-

from unittest import TestCase, skip

from basic_hw4_task_1 import country_filter
from basic_hw4_task_2 import ids_filter
from basic_hw4_task_3 import words_counter, persent_counter


class TestCountrysFilter(TestCase):
    
    def test_lower_case(self):
        visits = [
            {'visit1': ['москва', 'россия']},
            {'visit2': ['дели', 'индия']},
            {'visit3': ['владимир', 'pоссия']}]
        
        result = country_filter(visits)

        current_result = [
            {'visit1': ['москва', 'россия']},
            {'visit3': ['владимир', 'pоссия']}]

        self.assertEqual(result, current_result)
        
    @skip(reason="testing")
    def test_apper_case(self):
        visits = [
            {'visit1': ['МОСКВА', 'РОССИЯ']},
            {'visit2': ['ДЕЛИ', 'ИНДИЯ']},
            {'visit3': ['ВЛАДИМИР', 'РОССИЯ']}]
        
        result = country_filter(visits)

        current_result = [
            {'visit1': ['МОСКВА', 'РОССИЯ']},
            {'visit3': ['ВЛАДИМИР', 'РОССИЯ']}]

        self.assertEqual(result, current_result)


class TestIDsFilter(TestCase):

    def test_nonetype(self):
        ids = {
            'user1': [213, 213, 213, 15, 213],
            'user2': [54, None, 119, 119, 119]}
        
        result = ids_filter(ids)

        self.assertIn(None, result)

    def test_empty_list(self):
        ids = {
            'user1': [213, 213, 213, 15, 213],
            'user2': [],
            'user3': [213, 98, 98, 35]}
        
        result = ids_filter(ids)

        self.assertEqual(result, [213, 15, 98, 35])


class TestCounter(TestCase):

    def test_empty_list(self):
        queries = []

        words_counter_ =  words_counter(queries)
        persent_counter_ = persent_counter(words_counter_)

        self.assertEqual(persent_counter_, {})

