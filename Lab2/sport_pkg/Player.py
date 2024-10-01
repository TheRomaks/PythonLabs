from .Statistics import Statistics


# Класс Игрок
class Player(Statistics):
    def __init__(self, name: str, goals: int = 0, assists: int = 0):
        self.name = name
        self.goals = goals
        self.assists = assists

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Goals must be a non-negative integer")
        self._goals = value

    @property
    def assists(self):
        return self._assists

    @assists.setter
    def assists(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Assists must be a non-negative integer")
        self._assists = value

    def calculate_statistics(self):
        return {
            "name": self.name,
            "goals": self.goals,
            "assists": self.assists,
        }

    def __eq__(self, other):
        return self.name == other.name and self.goals == other.goals and self.assists == other.assists

    def __str__(self):
        return f"Игрок {self.name} забил {self.goals} голов и совершил {self.assists} ассистов"
