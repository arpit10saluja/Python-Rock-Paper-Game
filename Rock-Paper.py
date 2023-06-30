import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    user_score = 0
    computer_score = 0
    draws = 0

    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors), or 'q' to quit: ").lower()
        
        if user_choice == 'q':
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue
        
        computer_choice = random.choice(choices)
        
        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)
        
        if user_choice == computer_choice:
            print("It's a draw!")
            draws += 1
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        print("Score - You: {}, Computer: {}, Draws: {}\n".format(user_score, computer_score, draws))

play_game()
