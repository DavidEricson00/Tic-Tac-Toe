x = 0
y = 0
turn = 1

table = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def print_table():
    print("\n  1   2   3")
    for i, row in enumerate(table):
        print(f"{i + 1} " + " | ".join(row))
        if i < 2:
            print("  ---------")

while True:
    print_table()
    x = int(input('Select the line to place (1-3): '))
    y = int(input('Select the column to place (1-3): '))

    if x < 1 or x > 3 or y < 1 or y > 3:
        print("Invalid value, please try again.")
        continue

    elif table[x-1][y-1] != ' ':
        print("Position already occupied, please try again.")
        continue

    else:
        if turn % 2 == 0:
            table[x-1][y-1] = 'O'
        else:
            table[x-1][y-1] = 'X'

        turn += 1


