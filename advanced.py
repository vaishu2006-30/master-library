from calculator_basic.operations import add, subtract

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate_all(a, b):
    return {
        "add": add(a, b),
        "subtract": subtract(a, b),
        "multiply": multiply(a, b),
        "divide": divide(a, b)
    }