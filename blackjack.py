from random import choice
import os
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
player_hand = []
ai_hand = []
player_score = 0
ai_score = 0

def clear_screen():
    os.system('clear')

def deal_card(hand):
    hand.append(choice(deck))
    return hand

def init_game():
    player_hand = []
    ai_hand = []
    player_hand = deal_card(player_hand)
    player_hand = deal_card(player_hand)
    ai_hand = deal_card(ai_hand)
    ai_hand = deal_card(ai_hand)
    return player_hand, ai_hand
    

def calculate_score(hand):
    score = 0
    for card in hand:
        score += card
        
    if score > 21 and 11 in hand:
        score -= 10
        
    return score

def endgame(player, ai):
    player_score = calculate_score(player)
    ai_score = calculate_score(ai)
    
    if player_score == 21:
        print("Blackjack! You Win!")
    elif player_score > 21:
        print("Bust! You lose")
    else:
        while ai_score < 17:
            ai = deal_card(ai)
            ai_score = calculate_score(ai)
        
        ai_score = calculate_score(ai_hand)
        
        if ai_score > 21:
            print("The AI busts! You Win!")
        elif ai_score == player_score:
            print("Tie")
        elif ai_score > player_score:
            print('You lose')
        else:
            print('You Win!')
            

def game ():
    keep_playing = True
    print("Welcome to BlackJack!")
    
    while keep_playing:
        clear_screen()
        player_hand, ai_hand = init_game()
        player_score = 0
        ai_score = 0
        hitting = True
        
        print(f'Your hand: {player_hand}\n   Curent score: {player_score} The AI\'s hand: {ai_hand[0:1]}')
       
        if input('Would you like to hit or stay? (h/s)\n') == 's':
            hitting = False
        
        while hitting == True:
            player_hand = deal_card(player_hand)
            player_score = calculate_score(player_hand)
            if player_score >= 21:
                break
            
            print(f'Your hand: {player_hand}\n   Curent score: {player_score} The AI\'s hand: {ai_hand[0:1]}')
            if input('Would you like to hit or stay? (h/s)') == 's':
                hitting = False
                
        endgame(player_hand, ai_hand)
        if input("Would you like to play again? (y/n)") == 'n':
            keep_playing = False
        
        
game() 