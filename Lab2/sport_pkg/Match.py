from .Statistics import Statistics
from .Team import Team


class Match(Statistics):
    def __init__(self, team1: Team, team2: Team, score1: int = 0, score2: int = 0):
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2

    @property
    def team1(self):
        return self._team1

    @team1.setter
    def team1(self, value):
        if not isinstance(value, Team):
            raise ValueError("Team must be an instance of Team")
        self._team1 = value

    @property
    def team2(self):
        return self._team2

    @team2.setter
    def team2(self, value):
        if not isinstance(value, Team):
            raise ValueError("Team must be an instance of Team")
        self._team2 = value

    @property
    def score1(self):
        return self._score1

    @score1.setter
    def score1(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Score must be a non-negative integer")
        self._score1 = value

    @property
    def score2(self):
        return self._score2

    @score2.setter
    def score2(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Score must be a non-negative integer")
        self._score2 = value

    def calculate_statistics(self):
        team1_stats = self.team1.calculate_statistics()
        team2_stats = self.team2.calculate_statistics()
        return {
            "team1": team1_stats,
            "team2": team2_stats,
            "score": f"{self.score1} - {self.score2}"
        }

    def __str__(self):
        return f"{self.team1.name} {self.score1} - {self.team2.name} {self.score2}"