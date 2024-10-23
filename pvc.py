# pvc.py
from util import clear_screen, machinedifmenu, header, heads_or_tails
from player import Player
from game import game

def menupvc():
    option = 0

    while option != 3: # Main Menu
        # Print menu elements

        header()
        machinedifmenu()
        
        try:
            option = int(input('Enter the desired option: ')) # Menu option input
            if option == 1:
                clear_screen()
                mainpvc("normal")
            elif option == 2:
                clear_screen()
                mainpvc("impossible")
            elif option != 3:
                clear_screen()
                print('Invalid option')

        except (ValueError, KeyboardInterrupt): # Handle non-integer and keyboard inputs
            clear_screen()
            print("Invalid input, please enter a number.")
    
    clear_screen()
    print('Returning to the main menu') # Exit mensage
    return

def mainpvc(difficulty):
    valid = None

    while not valid: # Player name check
        try:
            p_name = input("Enter the name of the player: ")
            valid = True
        except (ValueError, KeyboardInterrupt): # Handle non-integer and keyboard inputs
            clear_screen()
            print("Invalid name, please try again.")
        
    player1 = Player(p_name,'player')
    player2 = Player('Computer','computer',difficulty)

    clear_screen()

    if heads_or_tails(player1.name): 
        player1.set_turn(True) # Player 1 starts if win
        player2.set_turn(False)
    else:
        player1.set_turn(False)
        player2.set_turn(True) # Player 2 starts

    player1.choose_symbol()
    player2.symbol = 'O' if player1.symbol == 'X' else 'X'

    clear_screen()

    game(player1, player2)