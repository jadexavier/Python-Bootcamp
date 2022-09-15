import os

bidders = {}
auction_over = False

def bid():
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bidders[name] = bid
    
def winner(bids):
    win = 0
    win_bid = ''
    
    for name, bid in bids.items():
        if bid > win:
            win = bid
            win_bid = name
            
    return(win, win_bid)

while auction_over == False:
    
    bid()
    
    q = input("Are there any other bidders? (y/n)")
    
    if q == "n":
        auction_over = True
        
    os.system('clear')
        
win_person, win_value = winner(bidders)      
      
print(f"The winner is {win_person} with a bid of {win_value}.")