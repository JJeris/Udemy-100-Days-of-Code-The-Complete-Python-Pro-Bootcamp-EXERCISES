#Password Generator Project
from operator import ge
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# length = nr_letters+nr_symbols+nr_numbers

# for i in range(0, nr_letters):
#     password += letters[random.randint(0, len(letters)-1)]
#     print(i)

# for j in range(0, nr_symbols):
#     password += symbols[random.randint(0, len(symbols)-1)]

# for k in range(0, nr_numbers):
#     password += numbers[random.randint(0, len(numbers)-1)]
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = ""
length = nr_letters+nr_symbols+nr_numbers

for i in range(0, nr_letters):
    password += letters[random.randint(0, len(letters)-1)]
    print(i)

for j in range(0, nr_symbols):
    password += symbols[random.randint(0, len(symbols)-1)]

for k in range(0, nr_numbers):
    password += numbers[random.randint(0, len(numbers)-1)]

combined_subs = ""
for u in password:
    combined_subs+=u
    combined_subs+=","
arr = combined_subs.split(",")
arr.pop(-1)
random.shuffle(arr)

output = ""
# arr_len = len(arr)-1

for r in arr:
# while arr:
    # gen_index = random.randint(0, arr_len)
    # output+=arr[gen_index]
    # arr.remove(arr[gen_index])
    # arr_len-=1
    output+=r
print(output)  
    

# password = ""
# sub_let = ""
# sub_sym = ""
# sub_num = ""
# length = nr_letters+nr_symbols+nr_numbers
# for i in range(0, nr_letters):
#     sub_let += letters[random.randint(0, len(letters)-1)]
    
# for j in range(0, nr_symbols):
#     sub_sym += symbols[random.randint(0, len(symbols)-1)]
    
# for k in range(0, nr_numbers):
#     sub_num += numbers[random.randint(0, len(numbers)-1)]
    

# combined_subs = sub_let+sub_sym+sub_num
# combined_subs_arr = ""
# for u in combined_subs:
#     combined_subs_arr+=u
#     combined_subs_arr+=","
    
# combined_subs_arr = combined_subs_arr.split(",")
# combined_subs_arr.pop(-1)


# arr_len = len(combined_subs_arr) - 1
# while combined_subs_arr:
#       gen_index = random.randint(0, arr_len)
#       password+=combined_subs_arr[gen_index]
#       combined_subs_arr.remove(combined_subs_arr[gen_index])
#       arr_len-=1
# print(password)
# for g in range(0, length):
#     gen_index = random.randint(0, len(combined_subs)-1)
#     password+=combined_subs[gen_index]
    
# print(password)
