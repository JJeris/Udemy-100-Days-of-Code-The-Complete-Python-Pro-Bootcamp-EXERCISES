# Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
length = len(names)
generated_index = random.randint(0, length-1)
print(f"{names[generated_index]} is going to buy the meal today!")


