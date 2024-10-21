class Player:
    def __init__(self, name):
        self.name = name
        self.symbol = ''
        self.is_turn = False

    def choose_symbol(self):
        while self.symbol not in ['X', 'O']:
            self.symbol = input(f"{self.name}, you will play with X or O: ").upper()
            if self.symbol not in ['X', 'O']:
                print("Invalid symbol. Please choose either X or O.")

    def set_turn(self, is_turn):
        self.is_turn = is_turn
