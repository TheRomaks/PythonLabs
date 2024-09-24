#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set = set(garden)
# meadow_set = set(meadow)
# # TODO здесь ваш код
#
# # выведите на консоль все виды цветов
# # TODO здесь ваш код
# all_flowers = garden_set.union(meadow_set)
# print("Все виды цветов:", all_flowers)
#
# # выведите на консоль те, которые растут и там и там
# # TODO здесь ваш код
# common_flowers = garden_set.intersection(meadow_set)
# print("Цветы, растущие и там, и там:", common_flowers)
#
# # выведите на консоль те, которые растут в саду, но не растут на лугу
# # TODO здесь ваш код
# garden_only = garden_set.difference(meadow_set)
# print("Цветы, растущие только в саду:", garden_only)
#
# # выведите на консоль те, которые растут на лугу, но не растут в саду
# # TODO здесь ваш код
# meadow_only = meadow_set.difference(garden_set)
# print("Цветы, растущие только на лугу:", meadow_only)
def createSet(listsmth):
    return set(listsmth)

def uniteSets(set1, set2):
    return set1.union(set2)

def intersectionsSets(set1, set2):
    return set1.intersection(set2)

def diffSets(set1, set2):
    return set1.difference(set2)

def userSet():
    user_input = input("Введите элементы через пробел")
    return set(user_input.split())

def main():
    print("Выберите вариант:")
    print("1. Ввести  вручную")
    print("2. Использовать предопределенные значения")
    choice = input("Введите ваш выбор (1 или 2): ")

    if choice == '1':
        print("Сад:")
        oldGarden=userSet()
        print("Луг:")
        oldmeadow=userSet()
        print(oldGarden)
        print(oldmeadow)
    elif choice == '2':
        oldGarden=createSet(garden)
        oldmeadow=createSet(meadow)
        print(oldGarden)
        print(oldmeadow)
    else:
        print("Некорректный выбор. Используем предопределенные значения.")
        oldGarden = garden
        oldmeadow = meadow
        print(oldGarden)
        print(oldmeadow)
    unitedSet = uniteSets(oldmeadow, oldGarden)
    print(unitedSet)
    intersect = intersectionsSets(oldGarden, oldmeadow)
    print(intersect)
    diffm = diffSets(oldmeadow, oldGarden)
    diffg = diffSets(oldGarden, oldmeadow)
    print(f"{diffm}\n{diffg}")


if __name__ == "__main__":
    main()
