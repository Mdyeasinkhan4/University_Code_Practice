def evaluate_expressions(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for i, expr in enumerate(lines, start=1):
            expr = expr.strip()
            if expr == "":
                continue
            try:
                result = eval(expr)
                print(f"Expression {i}: {expr} = {result}")
            except Exception as e:
                print(f"Expression {i}: {expr} → Error")

    except FileNotFoundError:
        print("File not found!")


# Function call
evaluate_expressions("input.txt")
