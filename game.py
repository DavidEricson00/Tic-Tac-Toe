#game.py

def print_table(table):  # Print game table
    print("\n  1   2   3")
    for i, row in enumerate(table):
        print(f"{i + 1} " + " | ".join(row))
        if i < 2:
            print("  ---------")

def check_victory(table):  # Check for a winner
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != ' ':  # Row
            return table[i][0]
        if table[0][i] == table[1][i] == table[2][i] != ' ':  # Column
            return table[0][i]
    if table[0][0] == table[1][1] == table[2][2] != ' ':  # Main diagonal
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] != ' ':  # Secondary diagonal
        return table[0][2]
    return None  # No winner yet

def game(player1, player2):
    turn = 1  # Track turn number
    table = [[' ' for _ in range(3)] for _ in range(3)]  # Initialize table
    winner = None

    while turn <= 9 and not winner:  # Loop until win or draw
        print_table(table)
        current_player = player1 if player1.is_turn else player2  # Current player

        print(f"{current_player.name}'s turn [{current_player.symbol}]")

        try:
            x, y = current_player.coordenate()  # Get move

            if x < 0 or x > 2 or y < 0 or y > 2:  # Out of bounds
                print("Invalid value, try again.")

            elif table[x][y] != ' ':  # Position occupied
                print("Position occupied, try again.")

            else:
                table[x][y] = current_player.symbol  # Place symbol
                turn += 1  # Next turn

                winner = check_victory(table)  # Check winner

                if winner:  # Announce winner
                    print_table(table)
                    print(f"{current_player.name} wins!")
                    break

                # Swap turns
                player1.is_turn = not player1.is_turn
                player2.is_turn = not player2.is_turn

        except (ValueError, KeyboardInterrupt):  # Handle input errors
            print("\nInvalid input, enter a number.")

    if not winner:  # Draw case
        print_table(table)
        print("It's a draw!")
