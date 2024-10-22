# main.py

from util import header, mainmeunu, clear_screen
from pvp import mainpvp
from pvc import mainpvc

def main():
    option = 0

    while option != 3:
        header()
        mainmeunu()
        
        try:
            option = int(input('Enter the desired option: '))
            if option == 1:
                clear_screen()
                mainpvp()
            elif option == 2:
                clear_screen()
                mainpvc()
            elif option != 3:
                clear_screen()
                print('Invalid option')

        except (ValueError, KeyboardInterrupt):
            clear_screen()
            print("Invalid input, please enter a number.")
    
    print('Thanks for playing, goodbye.')

if __name__ == "__main__":
    main()