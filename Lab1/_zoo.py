#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from array import array
from logging import exception

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
# zoo.insert(1,'bear')
# print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
# zoo.extend(birds)
# print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
# zoo.remove('elephant')
# print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
# lion_index_for_people = zoo.index('lion') + 1
# lark_index_for_people = zoo.index('lark') + 1
# print(f"Лев сидит в клетке {lion_index_for_people}")
# print(f"Жаворонок сидит в клетке {lark_index_for_people}")

def add_animal(zoo,index,animal):
    zoo.insert(index,animal)

def remove_animal(zoo):
    animal = input("Введите имя животного, которое хотите убрать: ")
    if animal in zoo:
        zoo.remove(animal)
    else:
        print("Животного нет")


def add_bird(birds):
    bird = input("Введите имя птицы, которую хотите добавить: ")
    birds.append(bird)

def extendAnimals(zoo,birds):
    zoo.extend(birds)

def remove_bird(birds):
    bird = input("Введите имя птицы, которую хотите убрать: ")
    if bird in birds:
        birds.remove(bird)
    else:
        print("Птицы нет")

def animal_pos_for_people(zoo,animal):
    if animal in zoo:
        print(f"{animal} находится в клетке: {zoo.index(f'{animal}') + 1}")
    else:
        print("Нет животного в зоопарке")


def fillList():
    user_input = input("Введите элементы через пробел")
    return user_input.split()

def main():
    print("Выберите вариант:")
    print("1. Ввести  вручную")
    print("2. Использовать предопределенные значения")
    choice = input("Введите ваш выбор (1 или 2): ")

    if choice == '1':
        print("Введите животных в зоопарке:")
        zoo_list=fillList()
        print("Введите птиц:")
        birds_list=fillList()
    elif choice == '2':
        zoo_list=zoo
        birds_list=birds
    else:
        print("Некорректный выбор. Используем предопределенные значения.")
        zoo_list = zoo
        birds_list = birds
    add_animal(zoo_list,1,'bear')
    print(zoo_list)
    extendAnimals(zoo_list,birds_list)
    print(zoo_list)
    remove_animal(zoo_list)
    print(zoo_list)
    animal_pos_for_people(zoo_list,"bear")


if __name__ == "__main__":
    main()