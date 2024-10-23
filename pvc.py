# pvc.py

from util import clear_screen, heads_or_tails
from player import Player
from game import game

def mainpvc():
    valid = False

    while not valid:  # Player name input
        try:
            p_name = input("Enter the name of the player: ")
            valid = True
        except (ValueError, KeyboardInterrupt):  # Handle input errors
            clear_screen()
            print("Invalid name, try again.")
        
    # Define Player instances
    player1 = Player(p_name, 'player')
    player2 = Player('Computer', 'computer')  # Computer player

    clear_screen()

    # Heads or tails to determine who starts
    if heads_or_tails(player1.name):
        player1.set_turn(True)  # Player 1 starts
        player2.set_turn(False)
    else:
        player1.set_turn(False)
        player2.set_turn(True)  # Computer starts

    # Choose symbols for the players
    player1.choose_symbol()
    player2.symbol = 'O' if player1.symbol == 'X' else 'X'

    clear_screen()
    game(player1, player2)  # Start the game
