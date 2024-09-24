#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код

# first_songs_list=[
#     ['Halo', 4.9],
#     ['Enjoy the Silence', 4.20],
#     ['Clean', 5.83]
# ]
#
# total_time=round(sum(sumsongs[1] for sumsongs in first_songs_list),2)

#(f"Три песни звучат {total_time} минут")

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код

# sweetest_perfection_time = violator_songs_dict['Sweetest Perfection']
# policy_of_truth_time = violator_songs_dict['Policy of Truth']
# blue_dress_time = violator_songs_dict['Blue Dress']
#
# # Суммируем время звучания этих песен
# other_total_time = round(sweetest_perfection_time + policy_of_truth_time + blue_dress_time,2)

#print(f"А другие три песни звучат {other_total_time} минут")

def calculate_total_time(songs):
    return round(sum(song[1] for song in songs), 2)

def main():
    print("Доступные песни:")
    for idx, song in enumerate(violator_songs_list):
        print(f"{idx + 1}. {song[0]} - {song[1]} минут")

    # Запрос у пользователя на выбор песен
    selected_indices = input("Введите номера песен через запятую (например, 1,3,5): ")
    selected_indices = [int(idx.strip()) - 1 for idx in selected_indices.split(',')]

    # Формирование списка выбранных песен
    selected_songs = [violator_songs_list[idx] for idx in selected_indices if 0 <= idx < len(violator_songs_list)]

    # Расчет общего времени
    total_time = calculate_total_time(selected_songs)

    # Вывод результата
    print(f"Общее время звучания выбранных песен: {total_time} минут")

if __name__ == "__main__":
    main()
