#util.py

import os
import random

def clear_screen():  # Clear screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

def header():  # Game title
    print('---------------------------')
    print('        Tic-Tac-Toe        ')
    print('---------------------------')

def mainmenu():  # Main menu
    print('1. Player vs Player')
    print('2. Player vs Computer')
    print('3. Exit')

def machinedifmenu():  # PVC difficulty menu
    print('1. Normal')
    print('2. Impossible')
    print('3. Return')

def heads_or_tails(p):  # Heads or tails mechanic
    choice = ''
    options = ['heads', 'tails']

    print("To start the game, let's decide who's first.")

    while choice not in options:
        try:
            choice = input(f"{p}, heads or tails? ").strip().lower()

            if choice not in options:
                clear_screen()
                print('Invalid option, try again.')

        except (ValueError, KeyboardInterrupt):  # Handle input errors and interruption
            clear_screen()
            print("Invalid input, try again.")

    result = random.choice(options)

    if result == choice:  # Check result
        print(f'The result was {result}. {p} won!')
        return True

    print(f'The result was {result}. {p} lost.')
    return False






