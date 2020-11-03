var_1 = int(input('Введите 1-е число: '))
var_2 = int(input('Введите 2-ое число: '))
def my_function(var_1, var_2):
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        print('Деление на 0!')
print(my_function(var_1, var_2))
