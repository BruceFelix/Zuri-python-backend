import random

while True:
    possible_actions = ["R", "P", "S"]
    #getting user input
    user_action = input("Enter a choice (R for rock, P for paper, S for scissors): ").upper() #converts user input to uppercase
    while True:    
        if user_action not in possible_actions:
            while True:
                print("Wrong input")
                user_action = input("kindly choose a valid choice(R for rock, P for paper,  S for scissors): ").upper()
                if user_action in possible_actions:
                    break
        else:
            break
    # Computer chooses
    computer_action = random.choice(possible_actions)
    if user_action == "R":
        user_action = 'rock'
    elif user_action =='P':
        user_action = "paper"
    elif computer_action == 'S':
        computer_action = 'scissors'
    if computer_action == "R":
        computer_action = 'rock'
    elif computer_action =='P':
        computer_action = "paper"
    elif computer_action == 'S':
        computer_action = 'scissors'
    #printing user's selection to computer's choice
    print(f"\nPlayer ({user_action.capitalize()}): CPU ({computer_action.capitalize()}).\n")
    #choosing the winner
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        continue
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            break
        else:
            print("Rock smashes scissors! You lose.")
            break
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            break
        else:
            print("Paper covers rock! You lose.")
            break
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            break
        else:
            print("Scissors cuts paper! You lose.")
            break
