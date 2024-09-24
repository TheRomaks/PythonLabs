#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Папа','Мама','Брат']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Папа', 175],
    ['Мама', 170],
    ['Брат', 183]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print(f'Рост отца - {my_family_height[0][1]} см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
heightSum=sum([familymember[1] for familymember in my_family_height])
print(f'Общий рост семьи - {heightSum} см')

def get_family_data():
    my_family = []
    my_family_height = []

    num_members = int(input("Введите количество членов семьи: "))

    for _ in range(num_members):
        name = input("Введите имя члена семьи: ")
        height = int(input(f"Введите рост {name} в см: "))
        my_family.append(name)
        my_family_height.append([name, height])

    return my_family, my_family_height


def familyInfo(my_family_height):
    father_height = next((height for name, height in my_family_height if name == 'Папа'), 'не найден')
    print(f'Рост отца - {father_height} см')

    total_height = sum(member[1] for member in my_family_height)
    print(f'Общий рост моей семьи - {total_height} см')


def main():
    print("Выберите вариант:")
    print("1. Ввести радиус и точки вручную")
    print("2. Использовать предопределенные значения")
    choice = input("Введите ваш выбор (1 или 2): ")


    if choice == '1':
        myFamily, myFamilyHeight = get_family_data()
        familyInfo(myFamilyHeight)
    elif choice == '2':
        myFamily, myFamilyHeight=my_family,my_family_height
        familyInfo(myFamilyHeight)
    else:
        print("Некорректный выбор. Используем предопределенные значения.")
        myFamily, myFamilyHeight = my_family, my_family_height
        familyInfo(myFamilyHeight)

if __name__ == "__main__":
    main()