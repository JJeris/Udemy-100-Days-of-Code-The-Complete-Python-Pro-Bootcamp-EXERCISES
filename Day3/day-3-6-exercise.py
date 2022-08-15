# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
answer = input("You've come at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
while answer.lower()!="left" and answer.lower()!="right":
    print("Invalid choice.")
    answer = input("You've come at a cross road. Where do you want to go? Type \"left\" or \"right\" ")
if answer.lower() == 'left':
    answer = input("Youve come to a lake. There is an island in the middle of the lake. Type \"wait\" ot wait for a boat ot \"swim\" to attempt to swim to the island. ")
    while answer.lower()!="swim" and answer.lower()!="wait":
        # print("Invalid choice.")
        answer = input("Youve come to a lake. There is an island in the middle of the lake. Type \"wait\" ot wait for a boat ot \"swim\" to attempt to swim to the island. ")
    if answer.lower() == 'wait':
        answer = input("A boat soon comes and carries you over to the island. On it is a home with three doors - red, blue and yellow. Type \"red\", \"blue\" or \"yellow\" to enter any of the doors. ")
        # while answer.lower()!="red" or answer.lower()!="blue" or answer.lower()!="yellow":
        #     print("Invalid choice.")
        #     input("A boat soon comes and carries you over to the island. On it is a home with three doors - red, blue and yellow. Type \"red\", \"blue\" or \"yellow\" to enter any of the doors.")
        
        if answer.lower() == 'red':
            print("You were burned by fire. Game Over")
        elif answer.lower() == 'blue':
            print("You were eaten by beasts. Game Over.")
        elif answer.lower() == 'yellow':
            print("You win!")
        else:
            print("Game Over.")
    else:
        print("You were attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")