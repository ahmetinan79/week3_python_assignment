import random

turn = random.randint(0, 1)
x_status = []
o_status = []
move = []
game_on = 1

board = [['___', '___', '___'], ['___', '___', '___'], ['___', '___', '___']]

win = [[[0, 0], [0, 1], [0, 2]],
       [[1, 0], [1, 1], [1, 2]],
       [[2, 0], [2, 1], [2, 2]],
       [[0, 0], [1, 0], [2, 0]],
       [[0, 1], [1, 1], [2, 1]],
       [[0, 2], [1, 2], [2, 2]],
       [[0, 0], [1, 1], [2, 2]],
       [[0, 2], [1, 1], [2, 0]]]

print('Welcome to the Tic Tac Toe game.')
print('You will play against the computer.')
print("Player will use 'X', computer will use 'O'")
for item in board:
    print(*item)

while game_on == 1:

    if turn == 1:
        a = int(input('Player, please enter a number in range 0-2 for row coordinate: '))
        b = int(input('Player, please enter a number in range 0-2 for column coordinate: '))

        if (a in range(0, 3) and b in range(0, 3)) and ([a, b] not in x_status and [a, b] not in o_status):
            board[a][b] = ' X '
            for item in board:
                print(*item)
            move = [a, b]
            x_status.append(move)

            for c in win:
                x_three = [d for d in c if c in x_status]
                if len(x_three) == 3:
                    print('Congrats! Player won the game.')
                    game_on = 0

            else:
                if len(x_status) + len(o_status) == 9:
                    print('Game is a tie')
                    game_on = 0
                else:
                    turn = 0

        else:
            print('Player, please enter proper values for coordinates.')

    else:
        print("It is computer's turn.")
        if win[0][0] not in x_status and o_status:
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif win[0][2] not in x_status and o_status:
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif win[2][0] not in x_status and o_status:
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif win[2][2] not in x_status and o_status:
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)

        elif (win[0][0] and win[0][1] in o_status) and (win[0][2] not in x_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] and win[0][2] in o_status) and (win[0][1] not in x_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][1] and win[0][2] in o_status) and (win[0][0] not in x_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[1][0] and win[1][1] in o_status) and (win[1][2] not in x_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][0] and win[1][2] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[1][2] in o_status) and (win[1][0] not in x_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[2][0] and win[2][1] in o_status) and (win[2][2] not in x_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[2][0] and win[2][2] in o_status) and (win[2][1] not in x_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[2][1] and win[2][2] in o_status) and (win[2][0] not in x_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] and win[1][0] in o_status) and (win[2][0] not in x_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] and win[2][0] in o_status) and (win[1][0] not in x_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[1][0] and win[2][0] in o_status) and (win[0][0] not in x_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][1] and win[1][1] in o_status) and (win[2][1] not in x_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[0][1] and win[2][1] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[2][1] in o_status) and (win[0][1] not in x_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][2] and win[1][2] in o_status) and (win[2][2] not in x_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][2] and win[2][2] in o_status) and (win[1][2] not in x_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][2] and win[2][2] in o_status) and (win[0][2] not in x_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] and win[1][1] in o_status) and (win[2][2] not in x_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][0] and win[2][2] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[2][2] in o_status) and (win[0][0] not in x_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][2] and win[1][1] in o_status) and (win[2][0] not in x_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][2] and win[2][0] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[2][0] in o_status) and (win[0][2] not in x_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)

        elif (win[0][0] and win[0][1] in x_status) and (win[0][2] not in o_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] and win[0][2] in x_status) and (win[0][1] not in o_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][1] and win[0][2] in x_status) and (win[0][0] not in o_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[1][0] and win[1][1] in x_status) and (win[1][2] not in o_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][0] and win[1][2] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[1][2] in x_status) and (win[1][0] not in o_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[2][0] and win[2][1] in x_status) and (win[2][2] not in o_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[2][0] and win[2][2] in x_status) and (win[2][1] not in o_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[2][1] and win[2][2] in x_status) and (win[2][0] not in o_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] and win[1][0] in x_status) and (win[2][0] not in o_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] and win[2][0] in x_status) and (win[1][0] not in o_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[1][0] and win[2][0] in x_status) and (win[0][0] not in o_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][1] and win[1][1] in x_status) and (win[2][1] not in o_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[0][1] and win[2][1] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[2][1] in x_status) and (win[0][1] not in o_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][2] and win[1][2] in x_status) and (win[2][2] not in o_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][2] and win[2][2] in x_status) and (win[1][2] not in o_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][2] and win[2][2] in x_status) and (win[0][2] not in o_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] and win[1][1] in x_status) and (win[2][2] not in o_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][0] and win[2][2] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[2][2] in x_status) and (win[0][0] not in o_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][2] and win[1][1] in x_status) and (win[2][0] not in o_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][2] and win[2][0] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] and win[2][0] in x_status) and (win[0][2] not in o_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)

        elif win[1][1] not in x_status and o_status:
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)

        elif win[0][1] not in x_status and o_status:
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif win[2][1] not in x_status and o_status:
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif win[1][0] not in x_status and o_status:
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif win[1][2] not in x_status and o_status:
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)

        for c in win:
            o_three = [d for d in c if c in o_status]
            if len(o_three) == 3:
                print('Computer won the game.')
                game_on = 0
        else:
            if len(x_status) + len(o_status) == 9:
                print('Game is a tie')
                game_on = 0
            else:
                turn = 1