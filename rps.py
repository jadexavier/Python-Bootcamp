import random
options = ["rock", "paper", "scissors"]

#get player choices
p1choice = str.lower(input("Player 1 choose: "))
p2choice = random.choice(options)
print(f"The computer chose {p2choice}.")

    
#comparison logic
p1win = "Player 1 wins!"
p2win = "The computer wins!"

if p1choice == p2choice:
    print("It's a tie.")
   
elif p1choice == "rock":
    if p2choice == "scissors":
        print(p1win)
    elif p2choice == "paper":
        print(p2win)
        
elif p1choice == "paper":
    if p2choice == "rock":
        print(p1win)
    elif p2choice == "scissors":
        print(p2win)  

elif p1choice == "scissors":
    if p2choice == "paper":
        print(p1win)
    elif p2choice == "rock":
        print(p2win)    
else:
    print("Somebody tried to cheat")      