# Лабораторная работа 1
## Задания:
1. **`00_distance.py`**
   - **Задача:** Составить словарь словарей расстояний между городами
   - **Решение:**
   ```python
    def distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2) ** 0.5


    for city1 in sites:
        distances[city1] = {}
        for city2 in sites:
            if city1 != city2:
                distances[city1][city2] = distance(sites[city1], sites[city2])
            else:
                distances[city1][city2] = 0

    print(distances)
   ```

2. **`01_circle.py`**
    - **Задачи:**
    - Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
    - Если точка point лежит внутри того самого круга, то выведите на консоль True, Или False, в зависимости от того лежит точке в круге или нет
    - Аналогично для другой точки
    - **Решение:**
    ```python
    def circleArea(radius):
        print(round(math.pi * radius**2,4))
    def insideRadius(point,radius):
        print((point[0]**2 + point[1]**2) <=radius)
    radius = 42
    circleArea(radius)
    point_1 = (23, 34)
    insideRadius(point_1,radius)
    point_2 = (30, 30)
    insideRadius(point_2,radius)
    ```

3. **`02_operations.py`**
   - **Задача:** Расставьте знаки операций "плюс", "минус", "умножение" и скобки между числами "1 2 3 4 5" так, что бы получилось число "25"
   - **Решение:**
   ```python
   print(1+2*(3+4+5))
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
    my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

    first_film=my_favorite_movies[:10]
    last_film=my_favorite_movies[42:]
    second_film=my_favorite_movies[12:25]
    second_last_film=my_favorite_movies[35:40]

    print(first_film)
    print(last_film)
    print(second_film)
    print(second_last_film)
    ```

5. **`04_my_family.py`**
   - **Задача:** 
     - Выведите на консоль рост отца в формате "Рост отца - ХХ см"
     - Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
   - **Решение:**
    ```python
    my_family_height = [
    # ['имя', рост],
    ['Папа', 175],
    ['Мама', 170],
    ['Брат', 183]
    ]
    print(f'Рост отца - {my_family_height[0][1]} см')

    heightSum=sum([familymember[1] for familymember in my_family_height])
    print(f'Общий рост семьи - {heightSum} см')
    ```

6. **`05_zoo.py`**
   - **Задача:** 
     - Посадите медведя (bear) между львом и кенгуру
     - Добавьте птиц из списка birds в последние клетки зоопарка
     - Уберите слона
     - Выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
   - **Решение:**
     ```python
     zoo.insert(1, 'bear')
     print(zoo)
     zoo.extend(birds)
     print(zoo)
     zoo.remove('elephant')
     print(zoo)
     lion_index_for_people = zoo.index('lion') + 1
     lark_index_for_people = zoo.index('lark') + 1
     print(f"Лев сидит в клетке {lion_index_for_people}")
     print(f"Жаворонок сидит в клетке {lark_index_for_people}")
     ```

7. **`06_songs_list.py`**
   - **Задача:** 
     - Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате.
     - Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
   - **Решение:**
     ```python
      first_songs_list=[
      ['Halo', 4.9],
      ['Enjoy the Silence', 4.20],
      ['Clean', 5.83]
      ]

      total_time=round(sum(sumsongs[1] for sumsongs in first_songs_list),2)

      print(f"Три песни звучат {total_time} минут")
      
      sweetest_perfection_time = violator_songs_dict['Sweetest Perfection']
      policy_of_truth_time = violator_songs_dict['Policy of Truth']
      blue_dress_time = violator_songs_dict['Blue Dress']

      other_total_time = round(sweetest_perfection_time + policy_of_truth_time + blue_dress_time,2)

      print(f"А другие три песни звучат {other_total_time} минут")
     ```

8. **`07_secret.py`**
   - **Задача:** Расшифровать заданный шифр следую подсказкам.
   - **Решение:**
     ```python
      first = secret_message[0][3]
      second=secret_message[1][9:13]
      third=secret_message[2][5:15:2]
      fourth=secret_message[3][12:6:-1]
      fifth=secret_message[4][20:15:-1]

      res = f"{first} {second} {third} {fourth} {fifth}"
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
     garden_set = set(garden)
     meadow_set = set(meadow)
    
     all_flowers = garden_set.union(meadow_set)
     print("Все виды цветов:", all_flowers)
    
     common_flowers = garden_set.intersection(meadow_set)
     print("Цветы, растущие и там, и там:", common_flowers)
    
     garden_only = garden_set.difference(meadow_set)
     print("Цветы, растущие только в саду:", garden_only)
    
     meadow_only = meadow_set.difference(garden_set)
     print("Цветы, растущие только на лугу:", meadow_only)
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
     