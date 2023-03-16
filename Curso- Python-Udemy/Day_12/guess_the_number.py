import random
from art import logo

attempts = 10
number = random.randint(1, 100)

def atmpt_pt():
    a_p = print(f"You have {attempts} remaining to guess the number.")
    return a_p
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm Thinking of a number between 1 a 100.")

dificulty = input("Choose a dificulty. type 'easy' or 'hard': ")
if dificulty == "hard":
    attempts = 5
    atmpt_pt()
elif dificulty == "easy":
    attempts = 10
    atmpt_pt()
else:
    print("Invalid dificulty.\nTry again!")

while attempts > 0:
    guess = int(input("Make a Guess: "))
    attempts -= 1
    if attempts == 0:
        print(f"You have {attempts} attempts.\nGameOver")
        print(f"The answer is: {number}")
    elif guess == number:
        print(f"You got it!!\nYou guessed it in {attempts} attempts!")
        break
    elif guess < number:
        print("Too low.\nTry again!")
        atmpt_pt()
    elif guess > number:
        print("Too high.\nTry again!")
        atmpt_pt()
    elif guess == number - 2:
        print("Getting Hot.\nTry again!")
        atmpt_pt()
    elif guess == number + 2:
        print("Getting Hot.\nTry again!")
        atmpt_pt()

