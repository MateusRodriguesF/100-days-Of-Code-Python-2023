import random
from wordlist import list
from hangman_ascii import stgs
from replit import clear

# TODO-1 Randomly chosse a word from the wordlist and assign it to a variable callen chossen_word.

# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 Check if the letter the letter the user guessed (guess) is one of the letters in the chosen_word.

#TODO-4: - Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-5: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-6: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# Begin

logo = '''
                               
 _                             
| |_ ___ ___ ___ _____ ___ ___ 
|   | .'|   | . |     | .'|   |
|_|_|__,|_|_|_  |_|_|_|__,|_|_|
            |___|              
'''


lives = 6
game_over = False
display = []
word_list = list
stages = stgs

print("\n")
print(logo)
chossen_word = (random.choice(word_list))# word to a list with list()

word_lenght = len(chossen_word)
print(f"The Word has: {word_lenght} letters.\n")

for _ in range(len(chossen_word)):
    display += "_"
print(display)
print("\n")

while game_over == False:

    guess = input(f"Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You already guessed the letter {guess}")

    for position in range(len(chossen_word)):
        lttr = chossen_word[position]
        if lttr == guess:
            display[position] = lttr
            print(f"You guessed {guess}, that's Correct, keep going!")

    if guess not in chossen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life ")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")
            print(f"The Word is: {chossen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_over = True
        print("You Win!")

    # result = " ".join(str(e) for e in display)
    # print(result)
    print(stages[lives])




























    # for ltr in chossen_word:
    #     if ltr == guess:
    #         ltr = guess
    #         display_two.append(ltr)
    #     else:
    #         display_two.append("_", )
    # result = " ".join(str(e) for e in display)
    # print(result)
    # if result == chossen_word:
    #     game_over = True
    #     print("You win!")