#player.py

import random

class Player:
    def __init__(self, name, type):
        self.name = name  # Player name
        self.symbol = ''  # X or O
        self.is_turn = False  # Player turn
        self.type = type #Verify if its player or computer

    def choose_symbol(self):  # Choose X or O
        while self.symbol not in ['X', 'O']:
            try:
                self.symbol = input(f"{self.name}, you will play with X or O: ").upper()
                if self.symbol not in ['X', 'O']:
                    print("Invalid symbol. Choose X or O.")
            except (ValueError, KeyboardInterrupt):  # Handle input errors
                print("\nInvalid symbol. Choose X or O.")

    def set_turn(self, is_turn):  # Set turn
        self.is_turn = is_turn

    def coordenate(self):  # Get coordinates
        if self.type == 'player':
            try:
                x = int(input('[Select the line] (1-3): ')) - 1  # Adjust to 0-based
                y = int(input('[Select the column] (1-3): ')) - 1  # Adjust to 0-based
                return x, y
            except (ValueError, KeyboardInterrupt):  # Handle input errors
                print("Invalid input. Enter numbers 1 to 3.")
                return self.coordenate()  # Retry

        if self.type == 'computer':
            return random.randint(0, 2), random.randint(0, 2)