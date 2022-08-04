totalBill = float(input("What was the total bill?\n"))
percentage = float(input("What percentage would you like to tip?\n"))/100
numPeople = int(input("How many people are splitting the bill?\n"))

tip = totalBill * percentage
finalCost = totalBill + tip
split = round(finalCost/numPeople, 2)

print(f"Each person's share of the total is {split}.")