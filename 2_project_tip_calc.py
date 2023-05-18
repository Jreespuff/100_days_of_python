print('Welcome to the tip calculator.')
bill = float(input("What was the total bill? $ "))
tip = float(input("What percentage tip would you like to give? "))
split = float(input("How many people are you going to split the bill with? "))

tip = bill * (tip/100)
total = (bill + tip) / split
print("The total each person should pay is $" + str(round(total,2)))