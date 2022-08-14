# 🚨 Don't change the code below 👇
from typing import final


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

final_bill = 0;
if(size == "S"):
    final_bill+=15
    if(add_pepperoni == "Y"):
        final_bill+=2
elif(size == "M"):
    final_bill+=20
    if(add_pepperoni == "Y"):
         final_bill+=3
elif(size == "L"):
    final_bill+=25

if(extra_cheese == "Y"):
    final_bill+=1
    
print(f"Your final bill is ${final_bill}")
