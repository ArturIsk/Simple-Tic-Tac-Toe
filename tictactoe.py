smt = "         "
M = [[smt[i] for i in range(3)], [smt[i] for i in range(3, 6)], [smt[i] for i in range(6, 9)]]

print("-" * 9)
print(f'| {M[0][0]} {M[0][1]} {M[0][2]} |\n| {M[1][0]} {M[1][1]} {M[1][2]} |\n| {M[2][0]} {M[2][1]} {M[2][2]} |')
print("-" * 9)


counter_x = 0
counter_o = 0

list_x = []
list_o = []

play = True

while play is True:
    move = input('Please make a move: ')
    i = move[0]  # line
    j = move[2]  # column

    try:
        i = int(i)
        j = int(j)
        if M[i - 1][j - 1] != " ":
            print("The cell is occupied! Choose another one!")
        else:
            if counter_x == counter_o:
                M[i - 1][j - 1] = "X"
                counter_x += 1
                print("-" * 9)
                print(
                    f'| {M[0][0]} {M[0][1]} {M[0][2]} |\n| {M[1][0]} {M[1][1]} {M[1][2]} |\n| {M[2][0]} {M[2][1]} {M[2][2]} |')
                print("-" * 9)
            else:
                M[i - 1][j - 1] = "O"
                counter_o += 1
                print("-" * 9)
                print(
                    f'| {M[0][0]} {M[0][1]} {M[0][2]} |\n| {M[1][0]} {M[1][1]} {M[1][2]} |\n| {M[2][0]} {M[2][1]} {M[2][2]} |')
                print("-" * 9)
    except (IndentationError, SyntaxError, ValueError):
        print("You should enter numbers!")
    except IndexError:
        print("Coordinates should be from 1 to 3!")

    for i in range(3):
        if (M[i][0] == M[i][1] == M[i][2] and M[i][2] == "X") or (M[0][i] == M[1][i] == M[2][i] and M[2][i] == "X"):
            list_x.append(i)
        elif (M[i][0] == M[i][1] == M[i][2] and M[i][2] == "O") or (M[0][i] == M[1][i] == M[2][i] and M[2][i] == "O"):
            list_o.append(i)
        else:
            pass

    if M[0][0] == M[1][1] == M[2][2] or M[0][2] == M[1][1] == M[2][0]:
        if M[1][1] == "X":
            list_x.append("D")
            counter_x += 1
        elif M[1][1] == "O":
            list_o.append("D")
            counter_o += 1
        else:
            pass

    if len(list_x) > 0 and counter_x >= counter_o:
        print("X wins")
        play = False
    elif len(list_o) > 0:
        print("O wins")
        play = False
    elif len(list_x) == len(list_o) and counter_x == 5 and counter_o == 4:
        print("Draw")
        play = False
    else:
        pass