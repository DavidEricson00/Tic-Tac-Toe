import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
    print('---------------------------')
    print('        Tic-Tac-Toe        ')
    print('---------------------------')

def mainmeunu():
    print('1. Player vs Player')
    print('2. Player vs Machine')
    print('3. Exit')

def machinedifmenu():
    print('1. Normal')
    print('2. Impossible')
    print('3. return')