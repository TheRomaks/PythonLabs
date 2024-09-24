from _distance import main as dist
from  _circle import main as circ
from _operations import main as oper
from _favorite_movies import main as fav_mov
from _my_family import main as fam
from _zoo import  main as zoo
from _songs_list import main as song
from _secret import main as secr
from _garden import main as gard

tasks = [
    {"name": "Расстония между городами", "function": dist},
    {"name": "Задачи с окружностью", "function": circ},
    {"name": "Получить 25 из 5 цифр", "function": oper},
    {"name": "Показать любимые фильмы", "function": fav_mov},
    {"name": "Показать информацию о семье", "function": fam},
    {"name": "Работа в зоопарке", "function": zoo},
    {"name": "Списки песен", "function": song},
    {"name": "Расшифровка секретного сообщения", "function": secr},
    {"name": "Работа в саду", "function": gard}
]

def display_menu():
    print("\nМеню задач:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['name']}")

def main():
    while True:
        display_menu()
        choice = input("Выберите задачу (или введите 'quit' для выхода): ")
        if choice.lower() == 'quit':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(tasks):
                tasks[choice - 1]["function"]()
            else:
                print("Некорректный выбор. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
