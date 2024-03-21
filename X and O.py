def board(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = "_ _ _"
row2 = "_ _ _"
row3 = "_ _ _"

player1 = 'X'  
player2 = 'O'

def check_win():
    global row1, row2, row3
  
    for row in [row1, row2, row3]:
        if row[0] == row[2] == row[4] != '_':
            return True

    for i in range(3):
        if row1[i*2] == row2[i*2] == row3[i*2] != '_':
            return True
    
  
    if row1[0] == row2[2] == row3[4] != '_':
        return True
    if row1[4] == row2[2] == row3[0] != '_':
        return True
    
    return False

def check_draw():
    global row1, row2, row3
    return '_' not in row1 + row2 + row3

def check(p_row, p_column, player):
    global row1, row2, row3
    
    if p_row == 1:
        if p_column == 1:
            row1 = player + row1[1:]
        elif p_column == 2:
            row1 = row1[:2] + player + row1[3:]
        else:
            row1 = row1[:4] + player
    elif p_row == 2:
        if p_column == 1:
            row2 = player + row2[1:]
        elif p_column == 2:
            row2 = row2[:2] + player + row2[3:]
        else:
            row2 = row2[:4] + player
    else:
        if p_column == 1:
            row3 = player + row3[1:]
        elif p_column == 2:
            row3 = row3[:2] + player + row3[3:]
        else:
            row3 = row3[:4] + player

while True:
    board(row1, row2, row3)
    p1r = int(input("X Enter the row (1, 2, or 3): "))
    p1c = int(input("X Enter a column (1, 2, or 3): "))
    
    if p1r not in [1, 2, 3] or p1c not in [1, 2, 3]:
        print("Please enter 1, 2, or 3!")
        continue
    check(p1r, p1c, player1)
    
    board(row1, row2, row3)  
    
    if check_win():
        print("Player X wins!")
        break
    elif check_draw():
        print("It's a draw!")
        break
    
    p2r = int(input("O Enter the row (1, 2, or 3): "))
    p2c = int(input("O Enter a column (1, 2, or 3): "))
    if p2r not in [1, 2, 3] or p2c not in [1, 2, 3]:
        print("Please enter 1, 2, or 3!")
        continue
    check(p2r, p2c, player2)
    
    if check_win():
        board(row1, row2, row3)
        print("Player O wins!")
        break
    elif check_draw():
        board(row1, row2, row3)
        print("It's a draw!")
        break
