# -*- coding: utf-8 -*-


class Stack():
    def __init__(self) -> None:
        self.values = []

    def isEmpty(self) -> bool:
        """
        Проверка стека на пустоту.
        
        RETURN: bool
        """

        if self.values:
            return False
        return True

    def push(self, element: str) -> None:
        """
        Добавляет новый элемент на вершину стека.
        """

        self.values.append(element)

    def pop(self) -> str:
        """
        Удаляет верхний элемент стека. Стек изменяется.

        RETURN: last elenemt
        """

        return self.values.pop()

    def peek(self) -> str:
        """
        Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.

        RETURN: last element
        """
        
        return self.values[-1]

    def size(self) -> int:
        """
        Возвращает количество элементов в стеке.

        RETURN: count elements | int
        """
        
        return len(self.values)