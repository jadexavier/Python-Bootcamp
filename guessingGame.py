from random import randint

quit_condition = ""

while True:
    target = randint(1,25)
    guess = None
    
    while guess != target:
        guess = int(input("Guess a number between 1 and 25\n"))
        
        if guess == target:
            print("You win!")
        elif guess < target:
            print("Higher!")
        elif guess > target:
            print("Lower")
    
    print("Congratulations! Would you like to play again? y/n")
    quit_condition = input()
    
    if quit_condition == "n":
        break
