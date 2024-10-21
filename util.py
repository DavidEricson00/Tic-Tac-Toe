import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print('---------------------------')
    print('        Tic-Tac-Toe        ')
    print('---------------------------')

def mainmeunu():
    print('1. Player vs Player')
    print('2. Player vs Computer')
    print('3. Exit')

def machinedifmenu():
    print('1. Normal')
    print('2. Impossible')
    print('3. return')

def heads_or_tails(p):
    choice = ''
    options = ['heads', 'tails']

    print("To start the game let's decide who's the first to play by heads and tails")

    while choice not in options:
        choice = input(f"{p} do you choose heads or tails: ").lower()
        if choice not in ['heads', 'tails']:
            clear_screen()
            print('Invalid option, please try again')

    result = random.choice(options)

    if result == choice:
        print(f'The result was {result}, {p} won')
        return True
    print(f'The result was {result}, {p} lost')
    return False
