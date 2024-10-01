from typing import List
from .Player import Player
from .Statistics import Statistics


# Класс Команда
class Team(Statistics):
    def __init__(self, name: str, players: List[Player] = None):
        self.name = name
        self.players = players if players else []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def players(self):
        return self._players

    @players.setter
    def players(self, value):
        if not all(isinstance(player, Player) for player in value):
            raise ValueError("All players must be instances of Player")
        self._players = value

    def add_player(self, player: Player):
        self.players.append(player)

    def remove_player(self, player: Player):
        self.players.remove(player)

    def calculate_statistics(self):
        total_goals = sum(player.goals for player in self.players)
        return {
            "name": self.name,
            "total_goals": total_goals,
        }

    def __len__(self):
        return len(self.players)

    def __str__(self):
        return f"Команда {self.name} с составом {self.players}"