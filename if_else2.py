coins = int(input('введите монеты: '))
level = int(input('введите уровнь: '))
klass = input('введите клвсс персонажа: ')
quest_item = input('введите квестовый предмет: ')

if klass == 'гном' or klass == 'робот':
    print('вы прошли')
else:
    if (level > 9 and quest_item == 'пригласительное письмо') or (level < 10 and coins >= 100_000 and quest_item == 'пригласительное письмо'):
        print('вы прошли')
    else:
        print('вы не прошли')
