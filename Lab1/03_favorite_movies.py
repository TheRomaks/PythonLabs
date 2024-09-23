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

for q in list_movies(my_favorite_movies):
    print(q)