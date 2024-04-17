class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def brace_match(string):
    s = Stack()
    for i in string:
        if i in '({[':
            s.push(i)
        elif i in ')}]':
            if s.is_empty():
                return "Несбалансировано"
            if i == ")" and s.peek() == "(":
                s.pop()
            elif i == "]" and s.peek() == "[":
                s.pop()
            elif i == "}" and s.peek() == "{":
                s.pop()
            else:
                return "Несбалансировано"
    return "Сбалансировано" if s.is_empty() else "Несбалансировано"


if __name__ == "__main__":
    print(brace_match('(((([{}]))))'))
    print(brace_match('{{[(])]}}'))
