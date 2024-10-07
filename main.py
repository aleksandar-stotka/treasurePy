import random

print("Welcome to Rock, Paper, Scissors!\n")

player_wins = 0
computer_wins = 0

while True:
    # Player's input
    player = input("Enter a choice (rock, paper, scissors): ").lower()
    
    # Choices for the computer
    choices = ["rock", "paper", "scissors"]
    
    # Random choice for the computer
    computer = random.choice(choices)
    
    print(f"\nYou chose {player}, computer chose {computer}.")
    
    # If player and computer make the same choice
    if player == computer:
        print(f"Both players selected {player}. It's a tie!")
    
    # If player chooses rock
    elif player == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
            player_wins += 1
        else:
            print("Paper covers rock. You lose.")
            computer_wins += 1
    
    # If player chooses paper
    elif player == "paper":
        if computer == "rock":
            print("Paper covers rock! You win!")
            player_wins += 1
        else:
            print("Scissors cuts paper. You lose.")
            computer_wins += 1
    
    # If player chooses scissors
    elif player == "scissors":
        if computer == "paper":
            print("Scissors cuts paper! You win!")
            player_wins += 1
        else:
            print("Rock smashes scissors. You lose.")
            computer_wins += 1
    
    # Invalid input
    else:
        print("Invalid input! Please choose rock, paper, or scissors.")
    
    # Display the score
    print(f"\nScore: You {player_wins} - Computer {computer_wins}")
    
    # Ask if player wants to play again
    repeat = input("\nPlay again? (yes/no): ").lower()
    
    if repeat != "yes":
        print("Thanks for playing!")
        break
