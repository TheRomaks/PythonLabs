#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def circleArea(radius):
    return round(math.pi * radius**2,4)
def insideRadius(point,radius):
    return point[0]**2 + point[1]**2 <=radius**2
# Есть значение радиуса круга
# radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код
# circleArea(radius)

# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код
# insideRadius(point_1,radius)

# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код
# insideRadius(point_2,radius)


def userRadius():
    while True:
        try:
            radius = float(input("Введите радиус круга: "))
            return radius
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числовое значение.")

def userPoint():
    while True:
        try:
            x = float(input("Введите координату X точки: "))
            y = float(input("Введите координату Y точки: "))
            return (x, y)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите числовые значения.")

def main():
    print("Выберите вариант:")
    print("1. Ввести радиус и точки вручную")
    print("2. Использовать предопределенные значения")
    choice = input("Введите ваш выбор (1 или 2): ")

    if choice == '1':
        radius = userRadius()
        point1 = userPoint()
        point2 = userPoint()
    elif choice == '2':
        radius = 42
        point1 = (23, 34)
        point2 = (30, 30)
    else:
        print("Некорректный выбор. Используем предопределенные значения.")
        radius = 42
        point1 = (23, 34)
        point2 = (30, 30)

    # Calculate and print the area of the circle
    area = circleArea(radius)
    print(f"Площадь круга с радиусом {radius} равна: {round(area, 4)}")

    # Check and print if points are inside the circle
    print(f"Точка {point1} внутри круга: {insideRadius(point1, radius)}")
    print(f"Точка {point2} внутри круга: {insideRadius(point2, radius)}")

if __name__ == "__main__":
    main()

# Пример вывода на консоль:
#
# 77777.7777
# False
# False


