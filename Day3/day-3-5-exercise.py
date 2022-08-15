# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

THE_WORD_TRUE = "true"
THE_WORD_LOVE = "love"
names = name1.lower() + name2.lower()

def count_letter(word, name):
    number_of_word = 0
    number_of_word += name.count(word[0]) 
    number_of_word += name.count(word[1]) 
    number_of_word += name.count(word[2]) 
    number_of_word += name.count(word[3]) 
    return number_of_word

def output_result(result):  
    if result < 10 or result > 90:
        print(f"Your score is {result}, you go together like coke and mentos.")  
    elif result >= 40 and result <= 50:
        print(f"Your score is {result}, you are alright together.")    
    else:
        print(f"Your score is {result}")

def main():
    result = int(str(count_letter(THE_WORD_TRUE, names))+str(count_letter(THE_WORD_LOVE, names)))
    output_result(result)
main()