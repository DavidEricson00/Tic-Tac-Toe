from util import clear_screen, heads_or_tails

def mainpvp():
    p1 = ''
    p2 = ''

    p1 = str(input("Enter the name of the player 01: "))
    p2 = str(input("Enter the name of the player 02: "))
    clear_screen()
    
    print(heads_or_tails(p1))