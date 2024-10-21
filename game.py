# game.py
turn = 1
table = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_table(table):
    print("\n  1   2   3")
    for i, row in enumerate(table):
        print(f"{i + 1} " + " | ".join(row))
        if i < 2:
            print("  ---------")

def check_victory(table):
    for i in range(3):
        if table[i][0] == table[i][1] == table[i][2] != ' ':  # Line
            return table[i][0]
        if table[0][i] == table[1][i] == table[2][i] != ' ':  # Column
            return table[0][i]
    if table[0][0] == table[1][1] == table[2][2] != ' ':  # Main diagonal
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] != ' ':  # Secondary diagonal
        return table[0][2]
    return None

def game(player1, player2):
    turn = 1
    table = [[' ' for _ in range(3)] for _ in range(3)]
    
    while turn <= 9 and not check_victory(table):
        print_table(table)

        current_player = player1 if player1.is_turn else player2

        print(f"{current_player.name}'s turn ({current_player.symbol})")
        x = int(input('Select the line to place (1-3): '))
        y = int(input('Select the column to place (1-3): '))

        if x < 1 or x > 3 or y < 1 or y > 3:
            print("Invalid value, please try again.")
            continue

        elif table[x-1][y-1] != ' ':
            print("Position already occupied, please try again.")
            continue

        table[x-1][y-1] = current_player.symbol
        turn += 1

        winner = check_victory(table)
        if winner:
            print_table(table)
            print(f"{current_player.name} wins!")
            break

        # Troca de turnos
        player1.is_turn = not player1.is_turn
        player2.is_turn = not player2.is_turn

    if not winner:
        print_table(table)
        print("It's a draw!")