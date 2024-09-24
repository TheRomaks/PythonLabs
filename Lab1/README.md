# Лабораторная работа 1
## Задания:
1. **`00_distance.py`**
   - **Задача:** Составить словарь словарей расстояний между городами
   - **Решение:**
   ```python
    def distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5

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
   ```

2. **`01_circle.py`**
    - **Задачи:**
    - Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
    - Если точка point лежит внутри того самого круга, то выведите на консоль True, Или False, в зависимости от того лежит точке в круге или нет
    - Аналогично для другой точки
    - **Решение:**
    ```python
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
    ```

3. **`02_operations.py`**
   - **Задача:** Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25"
   - **Решение:**
   ```python
   def get25():
    print(1+2*(3+4+5))

   def main():
        get25()

   if __name__ == "__main__":
        main()
   ```

4. **`03_my_favorite_movies.py`**
   - **Задача:** 
     - Выведите на консоль с помощью индексации строки, последовательно:
       - первый фильм 
       - последний 
       - второй 
       - второй с конца
    - не выводить запятые, не использовать методы строк и не переопределять данную строку
    - **Решение:**
    - **Решение:**
    ```python
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
    ```

5. **`04_my_family.py`**
   - **Задача:** 
     - Выведите на консоль рост отца в формате "Рост отца - ХХ см"
     - Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
   - **Решение:**
    ```python
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
    ```

6. **`05_zoo.py`**
   - **Задача:** 
     - Посадите медведя (bear) между львом и кенгуру
     - Добавьте птиц из списка birds в последние клетки зоопарка
     - Уберите слона
     - Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
   - **Решение:**
     ```python
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
     ```

7. **`06_songs_list.py`**
   - **Задача:** 
     - Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате.
     - Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
   - **Решение:**
     ```python
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
     ```

8. **`07_secret.py`**
   - **Задача:** Расшифровать заданный шифр следую подсказкам.
   - **Решение:**
     ```python
      def printDecryptedMes():
        print("Зашифрованное сообщение")
        print(secret_message)
        first = secret_message[0][3]
        second=secret_message[1][9:13]
        third=secret_message[2][5:15:2]
        fourth=secret_message[3][12:6:-1]
        fifth=secret_message[4][20:15:-1]

        res = f"{first} {second} {third} {fourth} {fifth}"
        print("Расшифрованное сообщение")
        print(res)

      def main():
          printDecryptedMes()

      if __name__ == "__main__":
          main()

    ```

9. **`08_garden.py`**
   - **Задача:** 
     - Создайте множество цветов, произрастающих в саду и на лугу
     - Выведите на консоль все виды цветов
     - Выведите на консоль те, которые растут и там и там
     - Выведите на консоль те, которые растут в саду, но не растут на лугу
     - Выведите на консоль те, которые растут на лугу, но не растут в саду
   - **Решение:**
     ```python
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
     ```

10. **`09_shopping.py`**
    - **Задача:** Создайте словарь цен на продукты следующего вида (писать прямо в коде).     Указать надо только по 2 магазина с минимальными ценами
    - **Решение:**
      ```python
        sweets = {
            'печенье': [
                {'shop': 'ашан', 'price': 10.99},
                {'shop': 'пятерочка', 'price': 9.99}
            ],
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
      ```

11. **`10_store.py`**
    - **Задача:** Вывести стоимость каждого вида товара на складе, вручную без циклов.
    - **Реализация:**
      ```python
        table_code = goods['Стол']
        tables_quantity = store[table_code][0]['quantity'] + store[table_code][1]['quantity']
        tables_cost = (store[table_code][0]['quantity'] * store[table_code][0]['price']
                        + store[table_code][0]['quantity'] + store[table_code][1]['price'])
        print('Стол -', tables_quantity, 'шт, стоимость', tables_cost, 'руб')
        
        sofa_code = goods['Диван']
        sofas_quantity = store[sofa_code][0]['quantity'] + store[sofa_code][1]['quantity']
        sofas_cost = (store[sofa_code][0]['quantity'] * store[sofa_code][0]['price']
                        + store[sofa_code][0]['quantity'] + store[sofa_code][1]['price'])
        print('Диван -', sofas_quantity, 'шт, стоимость', sofas_cost, 'руб')
        
        chair_code = goods['Стул']
        chairs_quantity = store[chair_code][0]['quantity'] + store[chair_code][1]['quantity'] + store[chair_code][2]['quantity']
        chairs_cost = (store[chair_code][0]['quantity'] * store[chair_code][0]['price'] +
                        store[chair_code][1]['quantity'] * store[chair_code][1]['price'] +
                        store[chair_code][2]['quantity'] * store[chair_code][2]['price'])
        print('Стул -', chairs_quantity, 'шт, стоимость', chairs_cost, 'руб')
      ```
     