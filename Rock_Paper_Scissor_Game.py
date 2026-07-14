import random

play_again = "y"
while play_again == "y":
    attempt = 1
    player_score = 0
    computer_score = 0
    while attempt <= 3:
        choices = ["rock", "paper", "scissor"]
        computer_choice = random.choice(choices)

        player_choice = input("Enter rock, paper, or scissor: ").lower()
        if player_choice not in choices:
            print("Please enter rock, paper, or scissor.\n")
            continue
        if computer_choice == "rock" and player_choice == "paper":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print(f"You won Round: {attempt} \n ")
            player_score += 1
        elif computer_choice == "rock" and player_choice == "scissor":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print(f"Computer won Round: {attempt}\n ")
            computer_score += 1
        elif computer_choice == "rock" and player_choice == "rock":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print("Match Draw..!\n")
        elif computer_choice == "paper" and player_choice == "scissor":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print(f"You won Round: {attempt}\n ")
            player_score += 1
        elif computer_choice == "paper" and player_choice == "rock":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print(f"Computer won Round: {attempt}\n")
            computer_score += 1
        elif computer_choice == "paper" and player_choice == "paper":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print("Match Draw..!\n")
        elif computer_choice == "scissor" and player_choice == "rock":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print(f"You won Round: {attempt}\n ")
            player_score += 1
        elif computer_choice == "scissor" and player_choice == "paper":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print(f"Computer won Round: {attempt}\n ")
            computer_score += 1
        elif computer_choice == "scissor" and player_choice == "scissor":
            print(f"Your choice = {player_choice}")
            print(f"Computer choice = {computer_choice}\n")
            print("Match Draw..!\n")
        else:
            print("Please enter rock, paper, or scissor.")
        attempt += 1
    if player_score == 2 and computer_score == 1:
        print("YOU WON....!")
    elif player_score == 1 and computer_score == 2:
        print("COMPUTER WON! \nOops..Better Luck next time!")
    elif player_score == 0 and computer_score == 3:
        print("COMPUTER WON! \nBetter Luck next time!")
    elif player_score == 3 and computer_score == 0:
        print("Hooray YOU WON all three ROUNDS...!")
    else:
        print("Based on three Rounds..")
        print("MATCH DRAW!")
    try:
        play_again = input("Do you want to play again? (y/n): ").lower()
    except ValueError:
        print("please enter y or n")
    if play_again == "n":
        print("Thank you for playing!")