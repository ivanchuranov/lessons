inventory = [{'name': 'банан', "name": 'апельсин','name': 'яблоко'}]
inventory_price = [{'price': 1000, 'price': 500, 'price': 500}]
shop = [{'name': 'меч','price': '1000', 'name': 'алмаз'},{'price': '3000', 'name': 'глина','price': '500'}]
balance = 199999
shop_balance = 100000
shop_price = [{'price': '1000', 'price': '3000', 'price': '500'}]

# /show
# /show shop
# /balance
# /buy
# /sell
# /add balance
# /shop balance
# /add shop balance
k = 'name'
while True:
    cmd = input('>> ')
    if cmd == '/show':
        for i in range(len(inventory)):
            for k, v in inventory[i].items():
                print(f'{i + 1}. {v} - ', end='')
            for i in range(len(inventory_price)):
                for k, v in inventory_price[i].items():
                    print(f'{v} рублей ')
    elif cmd == '/balance':
        print(balance)
    elif cmd == '/add balance':
        money = int(input('введите сумму: '))
        balance += money
        print('ваш баланс пополнен!')
    elif cmd == '/add shop balance':
        money = int(input('введите сумму: '))
        shop_balance += money
        print('баланс магазина пополнен!')
    elif cmd == '/show shop':
        for i in range(len(shop)):
            for  k, v in shop[i].items():
                print(f'{i+1}. {v} - ', end= '')
            for i in range(len(shop)):
                for  k, v in shop[i].items():
                    print(f'{v} рублей ')
    elif cmd == '/sell':
        index = int(input('введите номер предмета на продажу: ')) - 1
        if shop_balance < int(inventory_price[index][index]):
            print('у покупателя недостаточно денег!')
        else:
            print('продажа прошла успешно!')
            balance += int(inventory_price[index][index])
            shop_balance -= int(inventory_price[index][index])
            shop.append(inventory[index][index])
            shop_price.append(inventory_price[index][index])
            del inventory[index][index]
            del inventory_price[index][index]
    elif cmd == '/shop balance':
        print(shop_balance)
    elif cmd == '/buy':
        items = int(input('введите номер предмета для покупки: ')) - 1
        if balance < int(shop_price[items]):
            print('у вас недостаточно денег!')
        else:
            print('покупка прошла успешно!')
            inventory_price.append(shop_price[items])
            inventory.append(shop[items])
            balance -= int(shop_price[items])
            del shop[items]
            del shop_price[items]
    elif cmd == '/q':
        break
    else:
        print("Такой команды не существует.")
