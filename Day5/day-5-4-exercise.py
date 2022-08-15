#Write your code below this row 👇

# CONSTANTS
START = 1
END = 101
EVAL_FIZZ = 3
EVAL_BUZZ = 5
MSG01 = "Fizz"
MSG02 = "Buzz"
MSG_COMBINED = MSG01+MSG02

# FUNCTIONS
def FizzBuzz(START, END, EVAL_FIZZ, EVAL_BUZZ, MSG01, MSG02, MSG_COMBINED):
    for i in range(START,END):
        if(i%EVAL_FIZZ==0 and i%EVAL_BUZZ==0):
            print(MSG_COMBINED)
        elif(i%EVAL_FIZZ==0):
            print(MSG01)
        elif(i%EVAL_BUZZ==0):
            print(MSG02)
        else:
            print(i)

# EXECUTION OF PROGRAM
FizzBuzz(START, END, EVAL_FIZZ, EVAL_BUZZ, MSG01, MSG02, MSG_COMBINED)
