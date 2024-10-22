#util.py

import os
import random

def clear_screen(): #Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def header(): # Game title
    print('---------------------------')
    print('        Tic-Tac-Toe        ')
    print('---------------------------')

def mainmeunu(): # Main menu
    print('1. Player vs Player')
    print('2. Player vs Computer')
    print('3. Exit')

def machinedifmenu(): # PVC Menu
    print('1. Normal')
    print('2. Impossible')
    print('3. return')

def heads_or_tails(p): # Heads or Tails mechanic
    choice = ''
    options = ['heads', 'tails']

    print("To start the game let's decide who's the first to play by heads and tails")

    while choice not in options: # Heads or Tails pick
        try:
            choice = input(f"{p} do you choose heads or tails: ").lower()

            if choice not in ['heads', 'tails']:
                clear_screen()
                print('Invalid option, please try again')

        except (ValueError, KeyboardInterrupt): # Handle non-integer and keyboard inputs
            clear_screen()
            print("Invalid, please try again.")

    result = random.choice(options) # Draw a result

    if result == choice: # Win or Lose check
        print(f'The result was {result}, {p} won')
        return True
    
    print(f'The result was {result}, {p} lost')
    return False