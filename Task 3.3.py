def my_func(el_1, el_2, el_3):
    my_list = [el_1, el_2, el_3]
    my_list.pop(my_list.index(min(my_list)))
    return sum(my_list)
print(my_func(1, 8, 4))