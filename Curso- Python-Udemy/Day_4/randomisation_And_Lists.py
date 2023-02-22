import random

#  randomisation 👇

# random_integer = random.randint(1, 10)
# print (random_integer)

# Heads Tails Challenge 👇
# i = 5
# while i > 0:
#     i -= 1
#     words = ["Heads", "Tails"]
#     print(random.choice(words))

# Lists 👇

# fruits = ["item1", "item2"]

# WHo will pay the Bill Challenge 👇

# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")

# names_Len = len(names)
# rnd_numb = random.randint(0, names_Len - 1)

# luck_Guy = (names[rnd_numb])
# print(f"{luck_Guy} is going to buy the meal today!")

# Nested Lists

# images = ["jpg", "gif", "png", "webp"]
# played = ["mp3", "mp4", "avi", "mkv"]

# files = [images, played]

# print(files)

# Treasure Map Challenge

# row1 = ["⬜️0","️⬜️1","️⬜️2"]
# row2 = ["⬜️3","⬜️4","️⬜️5"]
# row3 = ["⬜️️6","⬜️️7","⬜️ ️8"]
# map = [row1, row2, row3]

# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")

# horizontal = int(position[0])
# vertical = int(position[1])



# selected_row = map[vertical -1]
# selected_row[horizontal -1] = "X"

# print(f"{row1}\n{row2}\n{row3}")

# rock-paper-scissors Challenge 🪨🧻✂️ 👇

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

# Cpu
choice_list = [rock, paper, scissors]
cpu_choice = random.randint(0, 2)
cpu_result = choice_list[cpu_choice]

# Player
print("What do you choose?\nType:\n0 for ROCK 🪨\n1 for PAPER 🧻\n2 for SCISSORS ✂️.")
player_choice = int(input(": "))
usr_choice = choice_list[player_choice]

# Printing Choose
print(f"Player Choose:\n{usr_choice}")
print(f"Cpu Choose:\n{cpu_result}")

# Program logic
if player_choice == 0 and cpu_choice ==2:
    print("You Win!")
elif cpu_choice == 0 and player_choice ==2:
    print("You Lose!")
elif cpu_choice > player_choice:
    print("You Lose!")
elif player_choice > cpu_choice:
    print("you win!")
elif cpu_choice == player_choice:
    print("Its a Draw!")

# print(player_choice)
# print(cpu_choice)