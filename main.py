'''
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
    
    # Check if either player reaches a score of 3
    if player_wins == 3:
        print("\nCongratulations! You reached 3 wins. Game Over!")
        break
    elif computer_wins == 3:
        print("\nThe computer reached 3 wins. Game Over!")
        break
    
    # Ask if player wants to continue the game after each round
    repeat = input("\nPlay again? (yes/no): ").lower()
    
    if repeat != "yes":
        print("Thanks for playing!")
        break

'''
##############

# password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for char in range(0,nr_letters):
     password_list.append(random.choice(letters))    
     
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
    
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)
print(password_list)
password = ""

for char in password_list:
    password += char


print(f"ypur password is:  {password}")




    



   

                                
    
    
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
    
    
    
