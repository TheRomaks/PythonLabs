#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продукты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        {'shop': 'ашан', 'price': 10.99},
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
        {'shop': 'пятерочка', 'price': 9.99}
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
    'конфеты': [
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99},
    ],
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    'пирожное': [
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ]
}
#из магнита
def select_sweets_from_shop(sweets):
    magnit_sweets = {}
    for sweet, shops in sweets.items():
        selected_shops = [shop for shop in shops if shop['shop'] == 'магнит']
        if selected_shops:
            magnit_sweets[sweet] = selected_shops
    return magnit_sweets

def print_sweets(magnit_sweets):
    for sweet, shops in magnit_sweets.items():
        print(f"{sweet}:")
       for shop in shops:
            print(f"  - {shop['shop']}: {shop['price']}")

def main():
    selected_sweets = select_sweets_from_shop(sweets)
    print_sweets(selected_sweets)

if __name__ == "__main__":
    main()






