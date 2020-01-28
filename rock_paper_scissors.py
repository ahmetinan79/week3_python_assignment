import random  # We use random module to generate random numbers for computer's choice.

choices = {1: "Rock", 2: "Paper", 3: "Scissors"}  # We have a brief explanation of the game.
print("""Welcome to Rock-Paper-Scissors Game. You will play against the computer.
You are asked to enter a number between 1-3 to make a choice based on Rock = 1, Paper = 2, Scissor = 3. 
The winning rule is as follows: 
Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissors wins
Same item -> Tie, pick a number again\n""")

while True:  # We use a while loop to come back in case of tie in the game or for another game.
    players_choice = int(input("Please choose number between 1-3: "))  # We take input from the player.
    print(f"Player choice is {choices[players_choice]}\n")  # We print the player's choice.
    print("Now it's computer's turn")
    computer_choice = random.randint(1, 3)  # We generate a random number for computer's between 1-3.
    print(f"Computer choice is {choices[computer_choice]}\n")  # We print the computer's choice.

    if players_choice == computer_choice:  # We have a condition, if two players have the same choice.
        print("Tie, pick a number again.")  # In case of a tie, we go back to beginning and ask for new choices.
        continue
    else:  # We have conditional phrases based on the rules of the game.
        if choices[players_choice] == "Rock" and choices[computer_choice] == "Paper":
            print("Rock vs Paper -> Computer wins")
        elif choices[players_choice] == "Paper" and choices[computer_choice] == "Rock":
            print("Paper vs Rock -> Player wins")
        elif choices[players_choice] == "Rock" and choices[computer_choice] == "Scissors":
            print("Rock vs Scissors -> Player wins")
        elif choices[players_choice] == "Scissors" and choices[computer_choice] == "Rock":
            print("Scissors vs Rock -> Computer wins")
        elif choices[players_choice] == "Paper" and choices[computer_choice] == "Scissors":
            print("Paper vs Scissors -> Computer wins")
        elif choices[players_choice] == "Scissors" and choices[computer_choice] == "Paper":
            print(f"Scissors vs Paper -> Player wins")

    game_on = input("\nDo you want to play again? If you want to continue please enter Y: ").upper()
    #  If the player wants to play again, s/he enters Y. Otherwise, the game ends.
    if game_on == "Y":
        print("\nNew game begins...")
    else:
        break