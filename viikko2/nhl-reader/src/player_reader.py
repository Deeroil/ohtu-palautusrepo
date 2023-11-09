import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        self.players = []
        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)

    def get_players(self):
        return self.players
