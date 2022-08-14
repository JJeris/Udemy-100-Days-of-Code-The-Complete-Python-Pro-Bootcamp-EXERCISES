print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
while(percentage!=10 and percentage!=12 and percentage!=15):
    print("Invalid input")
    percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
split = round((bill_total*(percentage/100)+bill_total)/people, 2)
print(f"Each person should pay: ${split}")