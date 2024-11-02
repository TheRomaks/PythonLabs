def create_list(lists_len):
    print("Создание списка")
    list_items = []
    for i in range(lists_len):
        while True:
            try:
                a = int(input(f"Введите целое число {i+1}: "))
                list_items.append(a)
                break
            except ValueError as e:
                print(f"Ошибка: {e}. Пожалуйста, введите целое число.")
    return list_items

def multiply_lists(list1,list2):
    list_res=map(lambda x, y: x * y, list1, list2)
    return list_res

def main():
    try:
        list_count=int(input("Введите размер списков: "))
        if list_count < 3:
            raise Exception("Оба списка должны содержать минимум 3 элемента.")

        list1 = create_list(list_count)
        list2 = create_list(list_count)

        if list1 is None or list2 is None:
            raise Exception("С такими списками невозможно работать")

        result = multiply_lists(list1,list2)

        for i in range(3):
            print(next(result))
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()