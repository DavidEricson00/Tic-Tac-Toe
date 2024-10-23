import random
import time

class Player:
    def __init__(self, name, type, difficulty = ''):
        self.name = name  # Player name
        self.symbol = ''  # X or O
        self.is_turn = False  # Player Turn
        self.type = type
        self.difficulty = difficulty

    def choose_symbol(self):  # X or O input
        while self.symbol not in ['X', 'O']:
            try:
                self.symbol = input(f"{self.name}, you will play with X or O: ").upper()
                if self.symbol not in ['X', 'O']:
                    print("Invalid symbol. Please choose either X or O.")
            except (ValueError, KeyboardInterrupt):  # Handle non-integer and keyboard inputs
                print("\nInvalid symbol. Please choose either X or O.")

    def set_turn(self, is_turn):
        self.is_turn = is_turn  # Turn true or false

    def coordenate(self):  # Add 'self' as the first parameter
        if self.type == 'player':
            try:
                x = int(input('[Select the line to place] (1-3): ')) - 1  # Line (adjusted to 0-based index)
                y = int(input('[Select the column to place] (1-3): ')) - 1  # Column (adjusted to 0-based index)
                return x, y
            except (ValueError, KeyboardInterrupt):  # Handle invalid input
                print("Invalid input. Please enter numbers between 1 and 3.")
                return self.coordenate()  # Retry input

        if self.type == 'computer':
            if self.difficulty == 'normal':
                x = random.randint(0, 2)
                y = random.randint(0, 2)
                return x, y
            else:
                pass