#pvp.py

from util import clear_screen, heads_or_tails
from player import Player
from game import game

def mainpvp():
    valid = None

    while not valid:  # Player name check
        try:
            p1_name = input("Enter the name of player 01: ")
            p2_name = input("Enter the name of player 02: ")
            valid = True
        except (ValueError, KeyboardInterrupt):  # Handle input errors
            clear_screen()
            print("Invalid name, try again.")

    # Define Player instances
    player1 = Player(p1_name, 'player')
    player2 = Player(p2_name, 'player')

    clear_screen()

    # Heads or tails
    if heads_or_tails(player1.name):
        player1.set_turn(True)  # Player 1 starts
        player2.set_turn(False)
    else:
        player1.set_turn(False)
        player2.set_turn(True)  # Player 2 starts

    # Choose symbols
    player1.choose_symbol()
    player2.symbol = 'O' if player1.symbol == 'X' else 'X'

    clear_screen()
    game(player1, player2)  # Start game