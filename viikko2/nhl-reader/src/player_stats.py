class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self, nat):
        print(f"Players from {nat}")

        natplayers = []
        for player in self.players.players:
            if player.nationality == nat:
                natplayers.append(player)

        natplayers.sort(key=lambda x: x.points, reverse=True)
        return natplayers
