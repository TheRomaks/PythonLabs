import pytest
from sport_pkg import Player,Team,Match

class TestPlayer:
    def test_init(self):
        player = Player("Sanya", 5, 3)
        assert player.name == "Sanya"
        assert player.goals == 5
        assert player.assists == 3

    def test_invalid_name(self):
        with pytest.raises(ValueError):
            Player(123, 5, 3)

    def test_invalid_goals(self):
        with pytest.raises(ValueError):
            Player("John", -1, 3)

    def test_invalid_assists(self):
        with pytest.raises(ValueError):
            Player("Dmitry", 5, -1)

    def test_calculate_statistics(self):
        player = Player("John", 5, 3)
        stats = player.calculate_statistics()
        assert stats == {"name": "John", "goals": 5, "assists": 3}

    def test_eq(self):
        player1 = Player("Mark", 5, 3)
        player2 = Player("Mark", 5, 3)
        player3 = Player("Makar", 5, 3)
        assert player1 == player2
        assert player1 != player3

    def test_str(self):
        player = Player("Sanya", 5, 3)
        str_player=str(player)
        assert str_player == "Игрок Sanya забил 5 голов и совершил 3 ассистов"

class TestMatch:
    def test_init(self):
        team1 = Team("Team A")
        team2 = Team("Team B")
        match = Match(team1, team2, 2, 1)
        assert match.team1.name == "Team A"
        assert match.team2.name == "Team B"
        assert match.score1 == 2
        assert match.score2 == 1

    def test_invalid_team(self):
        with pytest.raises(ValueError):
            Match("Team A", "Team B", 2, 1)

    def test_invalid_score(self):
        team1 = Team("Team A")
        team2 = Team("Team B")
        with pytest.raises(ValueError):
            Match(team1, team2, -1, 1)

    def test_calculate_statistics(self):
        team1 = Team("Team A")
        team2 = Team("Team B")
        match = Match(team1, team2, 2, 1)
        stats = match.calculate_statistics()
        assert stats == {
            "team1": {"name": "Team A", "total_goals": 0},
            "team2": {"name": "Team B", "total_goals": 0},
            "score": "2 - 1"
        }

    def test_str(self):
        team1 = Team("Team A")
        team2 = Team("Team B")
        match = Match(team1, team2, 2, 1)
        str_match =str(match)
        assert  str_match == "Team A 2 - Team B 1"

class TestTeam:
    def test_init(self):
        team = Team("Team A")
        assert team.name == "Team A"
        assert team.players == []

    def test_invalid_name(self):
        with pytest.raises(ValueError):
            Team(123)

    def test_remove_player(self):
        team = Team("Team A")
        player = Player("John", 5, 3)
        team.add_player(player)
        team.remove_player(player)
        assert len(team.players) == 0

    def test_add_player(self):
        team = Team("Team A")
        player = Player("John", 5, 3)
        new_player=Player("Alexei", 2, 3)
        team.add_player(player)
        team.add_player(new_player)
        assert len(team.players) == 2

    def test_calculate_statistics(self):
        team = Team("Team A")
        player1 = Player("John Doe", 5, 3)
        player2 = Player("Jane Doe", 2, 1)
        team.add_player(player1)
        team.add_player(player2)
        stats = team.calculate_statistics()
        assert stats == {"name": "Team A", "total_goals": 7}

    def test_str(self):
        team = Team("Team A",[Player("John", 5, 3),Player("Jane", 2, 1)])
        str_team=str(team)
        assert str_team == "Команда Team A с составом: John, Jane"

