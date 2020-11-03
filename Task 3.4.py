# первый вариант
def my_pow_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return 'Enter float'
    return result
print(my_pow_func(5, -2))


# второй вариант
def my_pow_func(x, y):
    try:
        x = float(x)
        y = int(y)
        res = x
        for i in range(abs(y) - 1):
            res = res * x
        return 1 / res
    except ValueError:
        return 'Check value'
print(my_pow_func(5, -2))