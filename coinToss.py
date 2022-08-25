import random

def coin_toss():
   coin = random.randint(0,1)
   if coin == 1:
       return "Heads"
   else:
       return "Tails"

print(coin_toss())