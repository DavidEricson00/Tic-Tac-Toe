# pvp.py
from util import clear_screen, heads_or_tails
from player import Player
from game import game

def mainpvp():
    p1_name = input("Enter the name of the player 01: ")
    p2_name = input("Enter the name of the player 02: ")
    
    player1 = Player(p1_name)
    player2 = Player(p2_name)
    
    clear_screen()
    
    if heads_or_tails(player1.name):
        player1.set_turn(True)
        player2.set_turn(False)
    else:
        player1.set_turn(False)
        player2.set_turn(True)

    player1.choose_symbol()

    player2.symbol = 'O' if player1.symbol == 'X' else 'X'
    
    clear_screen()
    game(player1, player2)