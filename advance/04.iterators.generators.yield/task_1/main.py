# -*- coding: utf-8 -*-


class FlatIterator:

    def __init__(self, list_of_lists: list) -> None:
        self.list_of_lists = list_of_lists

    def __iter__(self):
        return self

    def __next__(self):
        if self.list_of_lists:

            for inner_list in self.list_of_lists:
                item = inner_list.pop(0)

                if not inner_list:
                    self.list_of_lists.pop(0)
                
                return item
                    
        else:
            raise StopIteration   


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