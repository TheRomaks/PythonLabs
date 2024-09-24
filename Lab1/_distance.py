#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря
def distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

# Заполнение словаря расстояний
def buildDict(sities):
    for city1 in sities:
        distances[city1] = {}
        for city2 in sities:
            if city1 != city2:
                distances[city1][city2] = distance(sities[city1], sities[city2])
            else:
                distances[city1][city2] = 0
    return distances


def userSities():
    sities = {}
    while True:
        city = input("Введите название города (или 'quit' для завершения): ")
        if city.lower() == 'quit':
            break
        x = int(input("Введите координату X для {}: ".format(city)))
        y = int(input("Введите координату Y для {}: ".format(city)))
        sities[city] = (x, y)
    return sities


def predefinedSites():
    return sites

def main():
    print("Выберите вариант:")
    print("1. Ввести города и координаты вручную")
    print("2. Использовать предопределенные города")
    choice = input("Введите ваш выбор (1 или 2): ")

    if choice == '1':
        sites = userSities()
    elif choice == '2':
        sites = predefinedSites()
    else:
        print("Некорректный выбор. Используем предопределенные города.")
        sites = predefinedSites()

    distances = buildDict(sites)
    print(distances)


if __name__ == "__main__":
    main()





