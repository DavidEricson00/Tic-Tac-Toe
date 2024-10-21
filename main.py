import sys
import random
from util import header, mainmeunu, clear_screen

def main():
    option = 0

    while option != 3:
        header()
        mainmeunu()
        option = int(input('Enter the desired option: '))

        if option == 1:
            clear_screen()
            print('1. Player vs Player')
        elif option == 2:
            clear_screen()
            print('2. Player vs Machine')
        elif option != 3:
            clear_screen()
            print('Invalid option')
    
    print('Thanks for playing, goodbye.')

if __name__ == "__main__":
    main()