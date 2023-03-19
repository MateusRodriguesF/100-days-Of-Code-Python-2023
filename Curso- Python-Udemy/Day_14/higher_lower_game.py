import random
from replit import clear
from game_data import data
from art import logo, vs


# Check if user is correct
def check_answer(guess, a_followers, b_followers):
    """Check if user is correct using IF statement"""
    if a_followers > b_followers:
        return guess == "a" # <===> if guess == "a": return True else: return False
    else:
        return guess == "b"  
          
# Format account data into printable format.
def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return(f"{account_name}, {account_description}, {account_country}")

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    # Generate a random account from the game data.
    account_a = account_b
    account_b  = random.choice(data)
    while account_a == account_b:
        account_b == random.choice(data)

    # Printing game information
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess.
    print("\n")
    guess = input("Who has more followers?\nType 'A' or 'B': ").lower()

    # Check if user is correct.
    ## Get follower count.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)

    # Feedback.
    if is_correct:
        score += 1
        print(f"You're Right! Current Score: {score}\n")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}\n")
        continue_play = input("Want to play again?:\nType 'Y' to yes or 'N' to no: ").lower()
        if continue_play == "y":
            game_should_continue
            score = 0
        elif continue_play == "n":
            game_should_continue = False
        else:
            print("Invalid Option")
            game_should_continue = False

# My first code "solution" 🥲🥲🥲🥲🥲:
# game_data = data
# score = 0
# def get_person():
#     '''Returns a random person from a list with dictionary nested in'''
#     p_data = {}
#     p_data = random.choice(data) # take a random value and transform to a dictionary
#     person = list((p_data.values())) # transform to a list
#     return person

# def prnt_person():
#     persona = get_person()
#     persona.pop(1) # remove o indice [1] do dicionario
#     persona_str = ', '.join(map(str, persona)) # Transformar Lista em string
#     return persona_str

# def game():
#     print(logo)
#     p_1 = prnt_person()
#     p_2 = prnt_person()
#     print(f"Compare A: {p_1}")
#     print(vs)
#     print(f"Compare B: {p_2}")
#     guess = input("Who has more followers? Type 'A' or 'B': ").upper()
# game()