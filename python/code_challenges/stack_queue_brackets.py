from data_structures.stack import Stack


def multi_bracket_validation(string):
    square_stack = Stack()
    curly_stack = Stack()
    round_stack = Stack()
    for i in string:
        if i == "[":
            square_stack.push(i)
        if i == "]" and square_stack.is_empty():
            return False
        if i == "]" and not square_stack.is_empty():
            square_stack.pop()

        if i == "{":
            curly_stack.push(i)
        if i == "}" and curly_stack.is_empty():
            return False
        if i == "}" and not curly_stack.is_empty():
            curly_stack.pop()

        if i == "(":
            round_stack.push(i)
        if i == ")" and round_stack.is_empty():
            return False
        if i == ")" and not round_stack.is_empty():
            round_stack.pop()

    if square_stack.is_empty() and curly_stack.is_empty() and round_stack.is_empty():
        return True

    return False
