month = int(input('Введите месяц от 1 до 12: '))
my_dict = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}
print(my_dict.get(month))
my_list = ['зима', 'весна', 'лето', 'осень']
if month >= 1 and month <= 2 or month == 12:
    print(my_list[0])
if month >= 3 and month <= 5:
    print(my_list[1])
if month >= 6 and month <= 8:
    print(my_list[2])
if month >= 9 and month <= 11:
    print(my_list[3])


