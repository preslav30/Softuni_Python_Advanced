def operate(operator, *args):
    def addition(*args):
        result = 0
        for i in args:
            result += i
        return result

    def subtraction(*args):
        result = 0
        for i in args:
            result -= i
        return result

    def multiplication(*args):
        result = 1
        for i in args:
            result *= i
        return result

    def division(*args):
        result = 1
        for i in args:
            result /= i
        return result

    if operator == '+':
        return addition(*args)
    elif operator == '-':
        return subtraction(*args)
    elif operator == '*':
        return multiplication(*args)
    elif operator == '/':
        return division(*args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
