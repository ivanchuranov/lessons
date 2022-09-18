login = input('введите логин: ')
password = input('введите пароль: ')

if password == "abc":
    if login != "":
        print('добро пожаловать')
    else:
        print("Вы ввели пустой логин.")
else:
    print('вы ввели неправельный пароль.')


if password == "abc" and login != "":
    print('добро пожаловать')
else:
    print('не верные данные.')

