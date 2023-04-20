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

    def push(self, element: ...) -> None:
        """
        Добавляет новый элемент на вершину стека.
        """

        self.values.append(element)

    def pop(self) -> ...:
        """
        Удаляет верхний элемент стека. Стек изменяется.

        RETURN: last elenemt
        """

        return self.values.pop()

    def peek(self) -> ...:
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


#TESTING
stack = Stack()

# isEmpty
assert stack.isEmpty() == True

stack.values.append("first_value")
assert stack.isEmpty() == False

# push
stack.push("second_value")
assert stack.values == ["first_value", "second_value"]

stack.push("third_value")
assert stack.values == ["first_value", "second_value", "third_value"]

# pop
assert stack.pop() == "third_value"
assert stack.values == ["first_value", "second_value"]

# peek
assert stack.peek() == "second_value"
assert stack.values == ["first_value", "second_value"]

# size
assert stack.size() == 2