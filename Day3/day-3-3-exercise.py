# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if_leap = False
if(year%4 == 0):
    if(year % 100 == 0 and year % 400 == 0):
        if_leap = True
    elif(year % 100 == 0 and year % 400 != 0):
        if_leap = False
else:
    if_leap = False
    
if(if_leap == True):
    print("Leap year.")
else:
    print("Not leap year.")


