import random
from hangman_list import word_list
from hangman_art import stages

answer = list(random.choice(word_list))
solution = ["_" for x in range(0,len(answer))]
lives = 6
guesses = []

def output():
    print(stages[lives])
    print(''.join(solution))

while answer != solution and lives > 0:

    guess = input(("Choose a letter: "))
    if guess in answer:
        for char in range(len(answer)):
            if guess == answer[char]:
                solution[char] = guess
        output()
    else:
        lives -= 1
        output()

if lives == 0:
    final = ''.join(answer)
    print(f'You lose, the word was {final}')
else:
    print('You win!')