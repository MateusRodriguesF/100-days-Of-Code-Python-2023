# Utilizando Condicionais e controle de fluxo

# print("Wellcome to the RollerCoaster")
# height = int(input("Whats your height in cm?\n"))

# if height >= 120:
#     print("You can ride! 🎢 ")
# else:
#     print("You can not ride. 🥲 ")

# Utilizando Condicionais e controle de fluxo

# usr_num = int(input("Which number do you want to check?\n> "))

# if usr_num % 2 == 0:
#     print(f"The number {usr_num} is even.")
# else:
#     print(f"The number {usr_num} is odd.")

# IF aninhado e elif statement
# print("Wellcome to the RollerCoaster")
# height = int(input("Whats your height in cm?\n"))
# age = int(input("Whats your Age?\n"))

# if height >= 120:
#     print("You can ride! 🎢 ")
#     if age < 12:
#         print("You will pay $5")
#     elif age <= 18:
#         print("You will pay $7")
#     else:
#         print("You will pay $12")
# else:
#     print("You can not ride. 🥲 ")

# BMI cauculator 2.0

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# bmi = int(weight) / float(height) ** 2
# bmi_rnd = round(bmi) #aredondando o valor

# if bmi_rnd < 18.5:
#     print(f"Your bmi is {bmi_rnd}, you are underweight.")
# elif bmi_rnd < 25:
#     print(f"Your bmi is {bmi_rnd}, you have a normal weight.")
# elif bmi_rnd < 30:
#     print(f"Your bmi is {bmi_rnd}, you are slightly overweight.")
# elif bmi_rnd < 35:
#     print(f"Your bmi is {bmi_rnd}, you are obese.")
# else:
#     print(f"Your bmi is {bmi_rnd}, you are clinically obese.")

# leap year challenge
# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("Leap year.")
#     else:
#       print("Not leap year.")
#   else:
#     print("Leap year.")
# else:
#   print("Not leap year.")

# Mutiplos IF'S statements
# print("Wellcome to the RollerCoaster")
# height = int(input("Whats your height in cm?\n"))
# age = int(input("Whats your Age?\n"))
# bill = 0

# if height >= 120:
#     print("You can ride! 🎢 ")
#     if age < 12:
#         bill = 5
#         print(f"Child Tickets are {bill}")
#     elif age <= 18:
#         bill = 7
#         print(f"Youth Tickets are {bill}")
#     else:
#         bill = 12
#         print(f"Adults Tickets are {bill}")

#     want_photo = input("Do you want a photo taken? type Y or N. ")
#     if want_photo == "Y":
#         bill += 3
#     print(f"Your finall Bill is ${bill}")
# else:
#     print("You can not ride. 🥲 ")

# Pizza Challenge

print("Wellcome to Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill +=2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1

print(f"You Final Bill is ${bill}")


# Tue Love challenge

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

