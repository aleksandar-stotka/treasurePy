import random
print('Welcome to piper rock ')

choice = ['list',"karpa","nozici"]

computer_score = 0
player_score = 0

computer_choice = random.choice(choice)
print(f"computer choice is {computer_choice}")

player_choice = input("who is your choice list, karpa, or nozici? ")

print(player_choice)

if player_choice == computer_choice:
    print("is draw")
elif computer_choice == "list" or player_choice == "karpa":
    print("players win")
    player_score += 1
elif player_choice == "list" or computer_choice == "karpa":
     print("computer wins")
     computer_score =+ 1
     
print(f"computer score:{computer_score}  player score {player_score} ")    
   
    
     
    




