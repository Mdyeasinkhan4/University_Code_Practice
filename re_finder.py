import re

def calc (a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

s = "1+5+(3+2)"

vars = ''.join(sorted(set(re.findall('[a-z]', s))))
tokens = re.findall('[a-z]+|\d+|[+*/-]', s)

values, ops = [], []

for t in tokens:
    if t.isdigit():
        values.append(int(t))
    elif t.isalpha():
        continue

    else:
        if not values:
            continue

        while ops and (t in '+-' and ops[-1] in '*/'):
            b = values.pop()
            a = values.pop()
            values.append(calc(a, b, ops.pop()))
        ops.append(t)

while ops:
    if len(values) < 2:
        break
    b = values.pop()
    a = values.pop()
    values.append(calc(a, b, ops.pop()))

print(vars + str(int(values[0])))
