from replit import clear
############DEBUGGING#####################

# Describe Problem
#Solution: for i in range(0, 21):

# def my_function():
#   for i in range(0, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# Reproduce the Bug

# import random

# dice_imgs = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
# # dice_num = random.randint(1, 5)

# i = 30
# while i > 0:
#     i -= 1
#     dice_num = random.randint(0, 5)
#     print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age >= 18:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"Pages = {pages}")
# print(f"words per pages = {word_per_page}")
# print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])