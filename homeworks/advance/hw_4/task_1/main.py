# -*- coding: utf-8 -*-


class FlatIterator:

    def __init__(self, list_of_list: list) -> None:
        self.main_list = list_of_list

    def __iter__(self):
        self.main_cursor = 0
        self.sub_cursor = 0
        return self

    def __next__(self) -> any:
        for sub_list in self.main_list[self.main_cursor:]:
            for item in sub_list[self.sub_cursor:]:
                if len(sub_list) != self.sub_cursor + 1:
                    self.sub_cursor += 1
                else:
                    self.main_cursor += 1
                    self.sub_cursor = 0
                return item
                

def test_1() -> None:

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()