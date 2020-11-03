my_list = list(input('Введите список из 4-х элементов: '))
print(my_list)
n = len(my_list)
my_list.insert(0, my_list[1])
my_list.pop(2)
my_list.insert(2, my_list[3])
my_list.pop(4)
print(my_list)


