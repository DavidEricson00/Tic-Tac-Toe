# game.py

def print_table(table): # Table print
    print("\n  1   2   3")
    for i, row in enumerate(table):
        print(f"{i + 1} " + " | ".join(row))
        if i < 2:
            print("  ---------")

def check_victory(table):
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != ' ':  # Line check
            return table[i][0]
        if table[0][i] == table[1][i] == table[2][i] != ' ':  # Column check
            return table[0][i]
    if table[0][0] == table[1][1] == table[2][2] != ' ':  # Main diagonal check
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] != ' ':  # Secondary diagonal check
        return table[0][2]
    return None # Any win yet

def game(player1, player2):
    turn = 1  # Turn
    table = [[' ' for i in range(3)] for j in range(3)]  # Create table
    winner = None
    
    while turn <= 9 and not winner:  # Game loop, if table is full or someone wins, stop

        print_table(table)
        current_player = player1 if player1.is_turn else player2  # Check the player turn

        print(f"{current_player.name}'s turn [{current_player.symbol}]") # Player name and symbol

        try:
            x = int(input('[Select the line to place] (1-3): ')) # Line
            y = int(input('[Select the column to place] (1-3): ')) # Colum

            if x < 1 or x > 3 or y < 1 or y > 3: # Check if the coordenate is bigger than the array size
                print("Invalid value, please try again.")

            elif table[x-1][y-1] != ' ': # Check if the array is alredy occupied
                print("Position already occupied, please try again.")
            
            else:
                table[x-1][y-1] = current_player.symbol # Add symbol to array
                turn += 1 # Pass turn

                winner = check_victory(table) # Check win

                if winner: # Winner
                    print_table(table)
                    print(f"{current_player.name} wins!")
                    break

                # Swap turns only after a valid move
                player1.is_turn = not player1.is_turn
                player2.is_turn = not player2.is_turn

        except (ValueError, KeyboardInterrupt): # Handle non-integer and keyboard inputs
            print("\nInvalid input, please enter a number.")

    if not winner: # Draw
        print_table(table)
        print("It's a draw!")
