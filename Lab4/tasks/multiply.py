
def create_list(lists_len):
    list_items=[]
    for i in range(lists_len):
        a=int(input("Введите целое число: "))
        list_items.append(a)
    return list_items

def main():
    list1=create_list(3)
    list2=create_list(3)
    # list1 = [1, 2, 3, 4, 5]
    # list2 = [6, 7, 8, 9, 10]

    result = map(lambda x, y: x*y, list1,list2)

    for i in range(3):
        print(next(result))

if __name__ == "__main__":
    main()