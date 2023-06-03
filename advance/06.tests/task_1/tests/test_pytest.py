# -*- coding: utf-8 -*-

import pytest

from basic_hw4_task_1 import country_filter


@pytest.mark.parametrize(
    "visits, result", [
        ([{'visit1': ['Москва', 'Россия']}], [{'visit1': ['Москва', 'Россия']}]),
        ([{'visit1': ['Париж', 'Франция']}], []),
        ([{'visit1': ['Токио', 'Япония']}], []),
        ([{'visit1': ['Владимир', 'Россия']}], [{'visit1': ['Владимир', 'Россия']}])
    ])
def test_lower_case(visits, result):
    filtered = country_filter(visits)
    assert filtered == result