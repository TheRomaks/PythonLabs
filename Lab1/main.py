from _distance import main as dist
from  _circle import main as circ
from _operations import main as oper
from _favorite_movies import main as fav_mov
from _my_family import main as fam
from _zoo import  main as zoo
from _songs_list import main as song
from _secret import main as secr
from _garden import main as gard

def main():
    tasks = [
        {"name": "Расстония между городами", "function": dist()},
        {"name": "Задачи с окружностью", "function": circ()},
        {"name": "Получить 25 из 5 цифр", "function": oper()},
        {"name": "Показать любимые фильмы", "function": fav_mov()},
        {"name": "Показать информацию о семье", "function": fam()},
        {"name": "Работа в зоопарке", "function": zoo()},
        {"name": "Списки песен", "function": song()},
        {"name": "Расшифровка секретного сообщения", "function": secr()},
        {"name": "Работа в саду", "function": gard()}
    ]

    while True:
        print("Выберите задание:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['name']}")

        choice = input("Введите номер задания (или 'quit' для выхода): ")
        if choice == 'quit':
            return

        if choice.isdigit() and 1 <= int(choice) <= len(tasks):
            tasks[int(choice) - 1]["function"]()
        else:
            print("Данного задания нет в списке или вы ввели не число")

if __name__ == "__main__":
    main()
