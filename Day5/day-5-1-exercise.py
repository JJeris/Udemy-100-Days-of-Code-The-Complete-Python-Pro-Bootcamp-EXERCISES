# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum = 0
for height in student_heights:
    sum += height

length = 0
for i in student_heights:
    length+=1
    
avg = sum/length
print(f"The average height of the class is {int(avg)}")
    

#Write your code below this row 👇



