# 🚨 Don't change the code below 👇
from calendar import month


age = int(input("What is your current age?")) #changed
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90-age
months_left = years_left*12
weeks_left = years_left*52
days_left = years_left*365

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")







