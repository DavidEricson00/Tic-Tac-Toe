# pvc.py
from util import clear_screen, machinedifmenu, header


def mainpvc():
    option = 0

    while option != 3: # Main Menu
        # Print menu elements

        header()
        machinedifmenu()
        
        try:
            option = int(input('Enter the desired option: ')) # Menu option input
            if option == 1:
                clear_screen()
                print('Normal')
            elif option == 2:
                clear_screen()
                print('Impossible')
            elif option != 3:
                clear_screen()
                print('Invalid option')

        except (ValueError, KeyboardInterrupt): # Handle non-integer and keyboard inputs
            clear_screen()
            print("Invalid input, please enter a number.")
    
    clear_screen()
    print('Returning to the main menu') # Exit mensage
    return