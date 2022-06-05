class Frame:
    def __init__(self):
        self.rolls = []

    def is_strike(self, roll_index):
        return self.rolls[roll_index] == 10

    def is_spare(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10

    def strike_score(self, roll_index):
        return 10 + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

    def spare_score(self, roll_index):
        return 10 + self.rolls[roll_index + 2]

    def frame_score(self, roll_index):
        return self.rolls[roll_index] + self.rolls[roll_index + 1]
