# main.py

from util import header, mainmeunu, clear_screen
from pvp import mainpvp
from pvc import menupvc

def main():
    option = 0

    while option != 3: # Main Menu
        # Print menu elements
        header()
        mainmeunu()
        
        try:
            option = int(input('Enter the desired option: ')) # Menu option input
            if option == 1:
                clear_screen()
                mainpvp()
            elif option == 2:
                clear_screen()
                menupvc()
            elif option != 3:
                clear_screen()
                print('Invalid option')

        except (ValueError, KeyboardInterrupt): # Handle non-integer and keyboard inputs
            clear_screen()
            print("Invalid input, please enter a number.")
    
    print('Thanks for playing, goodbye.') # Exit mensage

if __name__ == "__main__":
    main()