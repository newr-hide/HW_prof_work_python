
class Stack():

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError('Стек пустой')
        else:
            return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# print(stack.is_empty())
# stack.push('(')
# print(stack.pop())
# print(stack.items)
# stack.push('(')
# stack.push('(')
# stack.push(')')
# print(stack.peek())
# print(stack.size())
# print(stack.items)

# Задание 2
# (((([{}]))))
# [([])((([[[]]])))]{()}
# {{[()]}}
# }{}
# {{[(])]}}
# [[{())}]

def balance(text):
    stack = Stack()

    for i in text:
        if i in ['(', '[', '{']:
            stack.push(i)
        elif not stack.is_empty():
            last_var = stack.pop()
            if (i == ')' and last_var != '(') or \
                    (i == ']' and last_var != '[') or \
                    (i == '}' and last_var != '{'):
                return False

    return True

text = input("Введите строку: ")
if balance(text):
  print("Сбалансированно")
else:
  print("Несбалансированно")


