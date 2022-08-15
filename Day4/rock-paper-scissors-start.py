rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user_input = int(input("What do you choose? 0 = Rock, 1 = Paper, 2 = Scissors."))
while(user_input!=0 and user_input!=1 and user_input!=2):
    print("Invalid input")
    user_input = input("What do you choose? 0 = Rock, 1 = Paper, 2 = Scissors.")
arr_of_choices = [rock, paper, scissors]
computers_choice = random.randint(0,2)
print(arr_of_choices[user_input])
print(arr_of_choices[computers_choice])
if user_input == 0 and computers_choice == 0:
    print("Draw!")
elif user_input == 0 and computers_choice == 2:
    print("You win!")
elif user_input == 0 and computers_choice == 1:
    print("You lose!") 
elif user_input == 1 and computers_choice == 0:
    print("You Win!")
elif user_input == 1 and computers_choice == 1:
    print("Draw!")
elif user_input == 1 and computers_choice == 2:
    print("You lose!")
elif user_input == 2 and computers_choice == 0:
    print("You lose!")
elif user_input == 2 and computers_choice == 1:
    print("You win!")
elif user_input == 2 and computers_choice == 2:
    print("Draw")