def generate_abs_numbers(a, b):
    for num in range(a, b + 1):
        yield abs(num)

def main():
    try:
        a = int(input("Введите целое число a: "))
        b = int(input("Введите целое число b (a < b): "))

        if a >= b:
            raise ValueError("a должно быть меньше b.")

        generator = generate_abs_numbers(a, b)

        for i in range(min(4, b - a + 1)):
            print(next(generator))
    except ValueError as e:
        print(f"Ошибка: {e}")
    else:
        print("Операция выполнена успешно.")

if __name__ == "__main__":
    main()