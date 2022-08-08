import random
options = ["rock", "paper", "scissors"]
player_score = 0
comp_score = 0
player_win = "Player wins!"
comp_win = "The computer wins!"
round = 1

print("Let's play Rock Paper Scissors!")
print("First to three wins")

while True:
   #get player choices
    print(f"Round {round}:")
    player_choice = str.lower(input("Choose a sign: "))
    while True:
        if player_choice == "rock" or player_choice == "scissors" or player_choice == "paper":
            break
        player_choice = str.lower(input("Choose a sign: rock, paper, or scissors: "))
    comp_choice = random.choice(options)
    print(f"The computer chose {comp_choice}.")

        
    #comparison logic
    if player_choice == comp_choice:
        print("It's a tie.")
    
    elif player_choice == "rock" and comp_choice == "scissors":
        print(player_win)
        player_score += 1
            
    elif player_choice == "paper" and comp_choice == "rock":
        print(player_win)
        player_score += 1

    elif player_choice == "scissors" and comp_choice == "paper":
        print(player_win)
        player_score += 1
    else:
        print(comp_win)
        comp_score += 1  
    
    round += 1
    
    if player_score == 3 or comp_score == 3 or round == 10:
        break   

if player_score == 3:
    print("Congratulations, you have bested the machine.")
elif comp_score == 3:
    print("Look what you've done. Hail Skynet.")
else:
    print("Holy shit how has it gone on this long???? Try again later.")