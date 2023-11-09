class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.nationality = dict['nationality']
        self.points = int(self.goals + self.assists)
    
    def __str__(self):
        return f"{self.name:20} {self.team:5} {self.goals:3} + {self.assists:2} = {self.points:3}"
