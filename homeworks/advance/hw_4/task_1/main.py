# -*- coding: utf-8 -*-


class FlatIterator:

    def __init__(self, list_of_lists: list) -> None:
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.outer_list_cursor = 0
        self.inner_list_cursor = 0
        return self

    def __next__(self) -> str | bool | None:

        if self.list_of_lists[self.outer_list_cursor:]:

            for inner_list in self.list_of_lists[self.outer_list_cursor:]:

                for item in inner_list[self.inner_list_cursor:]:

                    if len(inner_list) != self.inner_list_cursor + 1:
                        self.inner_list_cursor += 1
                    else:
                        self.outer_list_cursor += 1
                        self.inner_list_cursor = 0
                        
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