from sport_pkg import Player,Team,Match

def main():
    teams = []
    players = []
    matches = []

    while True:
        print("\nMenu:")
        print("1. Создать команду")
        print("2. Добавить игрока в команду")
        print("3. Создать матч")
        print("4. Отобразить статистику команды")
        print("5. Отобразить статистику игрока")
        print("6. Отобразить статистику матча")
        print("7. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            team_name = input("Введите название команды: ")
            team = Team(team_name)
            teams.append(team)
            print(f"Команда {team_name} создана.")

        elif choice == "2":
            if not teams:
                print("Нет команд. Перед созданием игрока, создайте спортивную команду.")
                continue

            print("Доступные команды:")
            for i, team in enumerate(teams):
                print(f"{i+1}. {team.name}")

            team_choice = int(input("Выберите команду в которой будет играть игрок: ")) - 1
            if team_choice < 0 or team_choice >= len(teams):
                print("Ошибка в выборе команды.")
                continue

            player_name = input("Введите имя игрока: ")
            goals = int(input("Введите количество голов: "))
            assists = int(input("Введите количество ассистов: "))

            player = Player(player_name, goals, assists)
            teams[team_choice].add_player(player)
            players.append(player)
            print(f"Игрок {player_name} добавлен в команду {teams[team_choice].name} .")

        elif choice == "3":
            if len(teams) < 2:
                print("Для создания матча необходимо наличие как минимум двух команд.")
                continue

            print("Доступные команды:")
            for i, team in enumerate(teams):
                print(f"{i+1}. {team.name}")

            team1_choice = int(input("Выберите первую команду: ")) - 1
            team2_choice = int(input("Выберите вторую команду: ")) - 1

            if team1_choice < 0 or team1_choice >= len(teams) or team2_choice < 0 or team2_choice >= len(teams):
                print("Invalid team choice.")
                continue

            score1 = int(input("Введите счёт первой команды: "))
            score2 = int(input("Введите счёт второй команды: "))

            match = Match(teams[team1_choice], teams[team2_choice], score1, score2)
            matches.append(match)
            print(f"Match between {teams[team1_choice].name} and {teams[team2_choice].name} created successfully.")

        elif choice == "4":
            if not teams:
                print("Нет команд.")
                continue

            print("Доступные команды:")
            for i, team in enumerate(teams):
                print(f"{i+1}. {team.name}")

            team_choice = int(input("Выберите команду чтобы отобразить статистику: ")) - 1
            if team_choice < 0 or team_choice >= len(teams):
                print("Ошибка в выборе команды.")
                continue

            print(teams[team_choice].calculate_statistics())

        elif choice == "5":
            if not players:
                print("Нет игроков.")
                continue

            print("Доступные игроки:")
            for i, player in enumerate(players):
                print(f"{i+1}. {player.name}")

            player_choice = int(input("Выберите игрока чтобы отобразить статистику: ")) - 1
            if player_choice < 0 or player_choice >= len(players):
                print("Ошибка в выборе игрока.")
                continue

            print(players[player_choice].calculate_statistics())

        elif choice == "6":
            if not matches:
                print("Нет матчей.")
                continue

            print("Доступные матчи:")
            for i, match in enumerate(matches):
                print(f"{i+1}. {match}")

            match_choice = int(input("Выберите матчи чтобы отобразить статистику: ")) - 1
            if match_choice < 0 or match_choice >= len(matches):
                print("Ошибка в выборе матча.")
                continue

            print(matches[match_choice].calculate_statistics())

        elif choice == "7":
            print("Выход.")
            break

        else:
            print("Ошибка. Выберите номер из списка")

if __name__ == "__main__":
    main()
