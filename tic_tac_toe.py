import random  # We import random module to generate random numbers to determine players'turn.

turn = random.randint(0, 1)  # We use a random number generator.
x_status = []  # We define a list to track player's moves.
o_status = []  # We define a list to track computer's moves.
move = []  # We define a temporary variable to record moves in each turn.
game_on = 1  # We define a key to continue or finish the while loop.

board = [['___', '___', '___'], ['___', '___', '___'], ['___', '___', '___']]  # We draw a board.

win = [[[0, 0], [0, 1], [0, 2]],  # We define every possible the winning situation.
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

while game_on == 1:  # We use a while loop for an ongoing game between two players.

    if turn == 1:  # If random number=1, then player starts the game.
        a = int(input('Player, please enter a number in range 0-2 for row coordinate: '))
        b = int(input('Player, please enter a number in range 0-2 for column coordinate: '))
        # We take two numbers from the player for coordinates.

        if (a in range(0, 3) and b in range(0, 3)) and ([a, b] not in x_status and [a, b] not in o_status):
            # We have a condition to verify that the coordinates are valid and the spot is not occupied.
            board[a][b] = ' X '  # We put the player's marker on the coordinates.
            for item in board:  # We print the board to see the current situation.
                print(*item)
            move = [a, b]  # We form a pair and record it into player's variable.
            x_status.append(move)

            for c in win:  # For loop checks if player's moves match any winning rows of three.
                x_three = [d for d in c if d in x_status]
                if len(x_three) == 3:
                    print('Congrats! Player won the game.')
                    game_on = 0

            else:  # There are 9 spots on the board and if the total of moves=9, then the game results in a tie.
                if len(x_status) + len(o_status) == 9:
                    print('Game is a tie')
                    game_on = 0
                else:  # If player does not win and it is not a tie, it is computer's turn.
                    turn = 0

        else:  # If the numbers that player enter do not meet the conditions, we ask for them again.
            print('Player, please enter proper values for coordinates.')

    else:
        print("It is computer's turn.")
        # In the fist part, computer checks if it can win with one move and the spot is not already occupied.
        if (win[0][0] in o_status and win[0][1] in o_status) and (win[0][2] not in x_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] in o_status and win[0][2] in o_status) and (win[0][1] not in x_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][1] in o_status and win[0][2] in o_status) and (win[0][0] not in x_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[1][0] in o_status and win[1][1] in o_status) and (win[1][2] not in x_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][0] in o_status and win[1][2] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in o_status and win[1][2] in o_status) and (win[1][0] not in x_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[2][0] in o_status and win[2][1] in o_status) and (win[2][2] not in x_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[2][0] in o_status and win[2][2] in o_status) and (win[2][1] not in x_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[2][1] in o_status and win[2][2] in o_status) and (win[2][0] not in x_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] in o_status and win[1][0] in o_status) and (win[2][0] not in x_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] in o_status and win[2][0] in o_status) and (win[1][0] not in x_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[1][0] in o_status and win[2][0] in o_status) and (win[0][0] not in x_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][1] in o_status and win[1][1] in o_status) and (win[2][1] not in x_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[0][1] in o_status and win[2][1] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in o_status and win[2][1] in o_status) and (win[0][1] not in x_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][2] in o_status and win[1][2] in o_status) and (win[2][2] not in x_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][2] in o_status and win[2][2] in o_status) and (win[1][2] not in x_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][2] in o_status and win[2][2] in o_status) and (win[0][2] not in x_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] in o_status and win[1][1] in o_status) and (win[2][2] not in x_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][0] in o_status and win[2][2] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in o_status and win[2][2] in o_status) and (win[0][0] not in x_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][2] in o_status and win[1][1] in o_status) and (win[2][0] not in x_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][2] in o_status and win[2][0] in o_status) and (win[1][1] not in x_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in o_status and win[2][0] in o_status) and (win[0][2] not in x_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        # In the second part, computer checks if it block the player and the spot is not already occupied.
        elif (win[0][0] in x_status and win[0][1] in x_status) and (win[0][2] not in o_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] in x_status and win[0][2] in x_status) and (win[0][1] not in o_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][1] in x_status and win[0][2] in x_status) and (win[0][0] not in o_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[1][0] in x_status and win[1][1] in x_status) and (win[1][2] not in o_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][0] in x_status and win[1][2] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in x_status and win[1][2] in x_status) and (win[1][0] not in o_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[2][0] in x_status and win[2][1] in x_status) and (win[2][2] not in o_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[2][0] in x_status and win[2][2] in x_status) and (win[2][1] not in o_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[2][1] in x_status and win[2][2] in x_status) and (win[2][0] not in o_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] in x_status and win[1][0] in x_status) and (win[2][0] not in o_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][0] in x_status and win[2][0] in x_status) and (win[1][0] not in o_status):
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif (win[1][0] in x_status and win[2][0] in x_status) and (win[0][0] not in o_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][1] in x_status and win[1][1] in x_status) and (win[2][1] not in o_status):
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif (win[0][1] in x_status and win[2][1] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in x_status and win[2][1] in x_status) and (win[0][1] not in o_status):
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif (win[0][2] in x_status and win[1][2] in x_status) and (win[2][2] not in o_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][2] in x_status and win[2][2] in x_status) and (win[1][2] not in o_status):
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)
        elif (win[1][2] in x_status and win[2][2] in x_status) and (win[0][2] not in o_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif (win[0][0] in x_status and win[1][1] in x_status) and (win[2][2] not in o_status):
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        elif (win[0][0] in x_status and win[2][2] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in x_status and win[2][2] in x_status) and (win[0][0] not in o_status):
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif (win[0][2] in x_status and win[1][1] in x_status) and (win[2][0] not in o_status):
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif (win[0][2] in x_status and win[2][0] in x_status) and (win[1][1] not in o_status):
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        elif (win[1][1] in x_status and win[2][0] in x_status) and (win[0][2] not in o_status):
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        # In the third part, the computer looks for the corners.
        elif win[0][0] not in x_status and win[0][0] not in o_status:
            board[0][0] = ' O '
            for item in board:
                print(*item)
            move = [0, 0]
            o_status.append(move)
        elif win[0][2] not in x_status and win[0][2] not in o_status:
            board[0][2] = ' O '
            for item in board:
                print(*item)
            move = [0, 2]
            o_status.append(move)
        elif win[2][0] not in x_status and win[2][0] not in o_status:
            board[2][0] = ' O '
            for item in board:
                print(*item)
            move = [2, 0]
            o_status.append(move)
        elif win[2][2] not in x_status and win[2][2] not in o_status:
            board[2][2] = ' O '
            for item in board:
                print(*item)
            move = [2, 2]
            o_status.append(move)
        # In the fourth part, the computer looks for the center.
        elif win[1][1] not in x_status and win[1][1] not in o_status:
            board[1][1] = ' O '
            for item in board:
                print(*item)
            move = [1, 1]
            o_status.append(move)
        # In the final part, the computer looks for the sides.
        elif win[0][1] not in x_status and win[0][1] not in o_status:
            board[0][1] = ' O '
            for item in board:
                print(*item)
            move = [0, 1]
            o_status.append(move)
        elif win[2][1] not in x_status and win[2][1] not in o_status:
            board[2][1] = ' O '
            for item in board:
                print(*item)
            move = [2, 1]
            o_status.append(move)
        elif win[1][0] not in x_status and win[1][0] not in o_status:
            board[1][0] = ' O '
            for item in board:
                print(*item)
            move = [1, 0]
            o_status.append(move)
        elif win[1][2] not in x_status and win[1][2] not in o_status:
            board[1][2] = ' O '
            for item in board:
                print(*item)
            move = [1, 2]
            o_status.append(move)

        for c in win: # For loop checks if computer's moves match any winning rows of three.
            o_three = [d for d in c if d in o_status]
            if len(o_three) == 3:
                print('Computer won the game.')
                game_on = 0
        else:  # There are 9 spots on the board and if the total of moves=9, then the game results in a tie.
            if len(x_status) + len(o_status) == 9:
                print('Game is a tie')
                game_on = 0
            else:  # If computer does not win and it is not a tie, it is player's turn.
                turn = 1