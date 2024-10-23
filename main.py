#main.py

# Functions and Libraries
from util import header, mainmenu, clear_screen
from pvp import mainpvp
from pvc import mainpvc

def main(): # Main function to display the menu and handle user interaction.

    option = 0

    while option != 3:  # Main Menu loop
        # Print menu elements
        header()
        mainmenu()

        try:
            option = int(input('Enter the desired option: '))  # Menu option input
            if option == 1:
                clear_screen()
                mainpvp()
            elif option == 2:
                clear_screen()
                mainpvc()
            elif option != 3:
                clear_screen()
                print('Invalid option, please try again.')

        except (ValueError, KeyboardInterrupt): # Handle non-integer and keyboard inputs
            clear_screen()
            print("Invalid input, please enter a number.")

    print('Thanks for playing, goodbye.')  # Exit message

if __name__ == "__main__":
    main()
