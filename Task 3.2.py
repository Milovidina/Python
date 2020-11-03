name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year_of_birth = (input('Введите год рождения: '))
city = input('Введите город рождения: ')
mail = input('Введите e-mail: ')
tel_number = input('Введите номер телефона: ')
def info_user(*kwargs):
    return kwargs
print(info_user(name, surname, year_of_birth, city, mail, tel_number))