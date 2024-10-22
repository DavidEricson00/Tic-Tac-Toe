#pvp.py

from util import clear_screen, heads_or_tails
from player import Player
from game import game

def mainpvp():
    # Names
    p1_name = input("Enter the name of the player 01: ")
    p2_name = input("Enter the name of the player 02: ")
    
    # Player Class
    player1 = Player(p1_name)
    player2 = Player(p2_name)
    
    clear_screen()
    
    # Heads or tails
    if heads_or_tails(player1.name): 
        player1.set_turn(True) # Player 1 starts if win
        player2.set_turn(False)
    else:
        player1.set_turn(False)
        player2.set_turn(True) # Player 2 starts

    # X or O class call
    player1.choose_symbol()

    # Player 2 Symbol
    player2.symbol = 'O' if player1.symbol == 'X' else 'X'
    
    clear_screen()
    game(player1, player2) # Start game