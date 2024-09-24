#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sign=','
# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код

def list_movies(fav_movie):
    comma_positions = [-2]
    for i in range(len(fav_movie)):
        if fav_movie[i] == sign:
            comma_positions.append(i)
    comma_positions.append(len(fav_movie))

    movies = [
        fav_movie[:comma_positions[1]],
        fav_movie[comma_positions[-2] + 2:],
        fav_movie[comma_positions[1] + 2:comma_positions[2]],
        fav_movie[comma_positions[-3] + 2:comma_positions[-2]],
    ]
    return movies
def userInput():
    my_fav_movies=input("Введите ваши любимые фильмы:")
    return  my_fav_movies
def printMovies(films):
    for q in list_movies(films):
        print(q)

def main():
    print("Выберите вариант:")
    print("1. Ввести фильмы вручную")
    print("2. Использовать предопределенные")
    choice = input("Введите ваш выбор (1 или 2): ")

    if choice == '1':
        films=userInput()
    elif choice == '2':
        films=my_favorite_movies
    else:
        print("Некорректный выбор. Используем предопределенные фильмы.")
        films=my_favorite_movies
    printMovies(films)


if __name__ == "__main__":
    main()