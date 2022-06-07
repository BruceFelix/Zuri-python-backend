import random

while True:
    possible_actions = {"R": 'rock', "P": 'paper', "S": 'scissors'}
    #getting user input
    user_action = input("Enter a choice (R for rock, P for paper, S for scissors): ").upper() #converts user input to uppercase
    while True:    
        if user_action not in possible_actions.keys():
            while True:
                print("Wrong input")
                user_action = input("kindly choose a valid choice(R for rock, P for paper,  S for scissors): ").upper()
                if user_action in possible_actions:
                    break
        else:
            break
    # Computer chooses
    computer_action = random.choice(list(possible_actions.keys()))
    #printing user's selection to computer's choice
    print(f"\nPlayer ({possible_actions[user_action].capitalize()}): CPU ({possible_actions[computer_action].capitalize()}).\n")
    #choosing the winner
    if user_action == computer_action:
        print(f"Both players selected {possible_actions[user_action]}. It's a tie!")
        continue
    elif possible_actions[user_action] == "scissors":
        if possible_actions[computer_action] == "paper":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break
    elif possible_actions[user_action] == "rock":
        if possible_actions[computer_action] == "scissors":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
            break
    elif possible_actions[user_action] == "paper":
        if possible_actions[computer_action] == "rock":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
