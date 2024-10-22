#player.py

class Player:
    def __init__(self, name):
        self.name = name # Player name
        self.symbol = '' # X or O
        self.is_turn = False # Player Turn

    def choose_symbol(self): # X or O input
        while self.symbol not in ['X', 'O']:
            self.symbol = input(f"{self.name}, you will play with X or O: ").upper()
            if self.symbol not in ['X', 'O']:
                print("Invalid symbol. Please choose either X or O.")

    def set_turn(self, is_turn):
        self.is_turn = is_turn # Turn true or false
