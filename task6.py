age = int(input('введите возраст: '))
login = input('введите логин: ')
password = input('введите пароль: ')

if age < 18:
    print("Извините, вам еще нет 18!")
else:
    print(f'Возраст: {age}, Логин: {login}, Пароль: {password}')