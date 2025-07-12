# david/calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b

def calculate(a, operator, b):
    if operator == '+':
        return add(a, b)
    elif operator == '-':
        return subtract(a, b)
    elif operator == '*':
        return multiply(a, b)
    elif operator == '/':
        return divide(a, b)
    else:
        print("Invalid operator.")
        return None

def parse_expression(expr):
    parts = expr.strip().split()
    if len(parts) != 3:
        print("Invalid expression format.")
        return None

    try:
        num1 = float(parts[0])
        op = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid number in expression.")
        return None

    if op not in ['+', '-', '*', '/']:
        print("Invalid operator.")
        return None

    if op == '/' and num2 == 0:
        print("Error: Division by zero.")
        return None

    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

def main():
    # 1) 기본 계산기: 정수 2개와 연산자 입력받아 계산
    try:
        a = int(input("Enter first integer: "))
        b = int(input("Enter second integer: "))
    except ValueError:
        print("Invalid input. Please enter integers.")
        return

    operator = input("Enter operator (+, -, *, /): ")
    result = calculate(a, operator, b)
    if result is not None:
        print(f"Result: {result}")

    # 2) 한 줄 수식 입력 받아 계산
    expr = input("\nEnter expression (e.g. 2 + 3): ")
    if expr.strip():
        expr_result = parse_expression(expr)
        if expr_result is not None:
            print(f"Result: {expr_result}")

if __name__ == "__main__":
    main()
