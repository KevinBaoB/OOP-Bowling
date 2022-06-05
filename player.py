from frame import Frame

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        
    def score(self):
        result = 0
        roll_index = 0
        for frame_index in range(10):
            if self.Frame.is_strike(roll_index):
                result += self.Frame.strike_score
                roll_index += 1
            elif self.is_spare(roll_index):
                result += self.Frame.spare_score
                roll_index += 2
            else: 
                result += self.Frame.frame_score(roll_index)
                roll_index += 2
        return result