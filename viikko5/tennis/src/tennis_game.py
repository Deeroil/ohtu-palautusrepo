class Player:
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name, 0)
        self.player2 = Player(player2_name, 0)


    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.score += 1
        else:
            self.player2.score += 1
    
    def _get_score_string(self, score):
        if score == 0:
            return "Love"
        elif score == 1:
            return "Fifteen"
        elif score == 2:
            return "Thirty"
        elif score == 3:
            return "Forty"
    
    def get_score(self):
        if self.player1.score == self.player2.score:
            if 2 >= self.player1.score >= 0:
                return f"{self._get_score_string(self.player1.score)}-All"
            else:
                return "Deuce"
        
        if self.player1.score >= 4 or self.player2.score >= 4:
            minus_result = self.player1.score - self.player2.score

            player = self.player1

            if minus_result < 0:
                player = self.player2

            if abs(minus_result) >= 2:
                return f"Win for {player.name}"

            if abs(minus_result) == 1:
                return f"Advantage {player.name}"
        
        p1_score = self._get_score_string(self.player1.score)
        p2_score = self._get_score_string(self.player2.score)
        return p1_score + "-" + p2_score

