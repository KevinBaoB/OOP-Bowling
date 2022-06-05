from player import Player
from frame import Frame

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player_name):
        self.players.append(player_name)

    def get_all_players(self):
        return self.players()

    def get_score_of_player(self, player_name):
        return player_name.player.score()