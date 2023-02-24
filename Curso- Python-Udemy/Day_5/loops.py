# Loops 👇
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit)

# Average height Challenge 👇
# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
# total = 0

# for height in student_heights:
#     total += height
# notes = len(student_heights)
# result = round(total / notes)
# print(result)

# Highest score challenge 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# high_score = 0
# for scr in student_scores:
#     if scr > high_score:
#         high_score = scr
# print(f"The highest score in the class is: {high_score}")

# # For loop with range👇
# for loop in range(1, 11):
#     print(loop)

# Range with steps 👇
# 2 em 2 ate 10
# for loop in range(1, 11, 3):
#     print(loop)

# Sum even numbers in a 1 to 100 list Challenge 👇
# My solution
# num_list = [*range(1, 101)]
# num_even = 0
# # print(num_list)
# for num in num_list:
#     if num % 2 == 0:
#         num_even += num
# print(num_even)

# # Course Solution
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# Fizz Buzz Challenge
# for num in range(1 ,101):
#     if num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     elif num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     else:
#         print(num)




# Final Project
# Password Generator Challenge
import random
import string
# Variables
letters = list(string.ascii_lowercase)
numbers = [*range(0, 10)]
symbols = ["*", "@", "#", "$", "%", "&", "!", "?"]

# Printing to screen
print("Wellcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

# Eazy Level

password = ""
for char in range(1, nr_letters + 1):
     password += random.choice(letters) 

for char in range(1, nr_numbers + 1):
     password += str(random.choice(numbers))

for char in range(1, nr_symbols + 1):
     password += random.choice(symbols)    
# print(password)

# hard level
# randomisation of the list

password_list = []
for char in range(1, nr_letters + 1):
     password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
     password_list.append(str(random.choice(numbers)))

for char in range(1, nr_symbols + 1):
     password_list.append(random.choice(symbols))    

# Reordering the list
random.shuffle(password_list)

# Final Result
rnd_psswd = ""
for char in password_list:
    rnd_psswd += char

# Password generated
print(f"Your Password is: {rnd_psswd}")