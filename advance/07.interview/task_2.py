# -*- coding: utf-8 -*-

from task_1 import Stack


opening_breckets = ["(", "[", "{"]
closing_breckets = [")", "]", "}"]

stack = Stack()

def check(breckets: str) -> str:

    for brecket in breckets:

        if brecket in opening_breckets:
            stack.push(brecket)

        elif brecket in closing_breckets:
            position = closing_breckets.index(brecket)

            if stack.size() > 0 and opening_breckets[position] == stack.peek():
                stack.pop()

            else:
                return "Несбалансированно"
        
    if stack.size() == 0:
        return "Сбалансированно"
    else:
        return "Несбалансированно"