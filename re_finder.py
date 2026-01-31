import re

def calc(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def precedence(op):
    if op in '+-': return 1
    if op in '*/': return 2
    return 0

s = "2+3*(5-3)+14/7"

# tokenization (numbers, operators, parentheses)
tokens = re.findall(r'\d+|[()+\-*/]', s)

values = []
ops = []

for t in tokens:
    if t.isdigit():
        values.append(int(t))

    elif t == '(':
        ops.append(t)

    elif t == ')':
        while ops and ops[-1] != '(':
            b = values.pop()
            a = values.pop()
            values.append(calc(a, b, ops.pop()))
        ops.pop()  # remove '('

    else:  # operator
        while ops and precedence(t) <= precedence(ops[-1]):
            b = values.pop()
            a = values.pop()
            values.append(calc(a, b, ops.pop()))
        ops.append(t)

while ops:
    b = values.pop()
    a = values.pop()
    values.append(calc(a, b, ops.pop()))

print(values[0])
