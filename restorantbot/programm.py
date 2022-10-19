from random import randint

class User:
    def __init__(self, chatid, first_name, username=None, last_name=None,role='client'):
        self.role = role
        self.chatid = chatid
        self.first_name = first_name
        self.username = username
        self.last_name = last_name


class Programm:
    def __init__(self):
        commands = {
            'client': [
            {'cmd': '/help',
             'info': 'выводит информацию о всех командах'},
            {'cmd': '/q',
             'info': 'выход из программы'},
            {'cmd': '/menu',
             'info': 'вывод меню'},
            {'cmd':'/order',
             'info': 'выбор'}],
            'admin': [
                {'cmd': '/ban',
                 'info': 'выводит информацию о всех командах'}]
        }
        self.current_user = self.Authorize()

    def Authorize(self):
        first_name = input('Введите имя: ')
        last_name = input('Введите фамилию: ')
        chatid = randint(1, 23908)

        username = input('Введите имя пользователя: ')

        role = input('Введите роль: ')

        if role != "":
            user = User(chatid, first_name, username, last_name, role)

        user = User(chatid, first_name, username, last_name)

        return user


    def cmd_handler_help(self):
        print('Добро пожаловать в наш Restaurant Bot!')

    def cmd_handler_menu(self):
        menu = [{'name': 'apple pie', 'price': 500}, {'name': 'cake', 'price': 1000}]
        for i in range(len(menu)):
            print(f'{i+1}. {menu[i]["name"]} - {menu[i]["price"]}')

    def cmd_handler(self, cmd):
        return False

    def CheckCommand(self):
        pass

    def start(self):
        while True:
            cmd = input('>>')
            if cmd == '/help':
                self.cmd_handler_help()
            elif cmd == '/q':
                break
            elif cmd == '/menu':
                self.cmd_handler_menu()
            elif not self.cmd_handler(cmd):
                print('Такой команды не существует.')

app = Programm()
app.start()0