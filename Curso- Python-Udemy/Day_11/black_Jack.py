import random
from replit import clear
from art import logo



def deal_card():
    """"Return random cards, the parameter rng is for set the range."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards e return the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """"Compare user and computer score!"""
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has BlackJack 👌"
    elif user_score == 0:
        return "Win with a BlackJack 👍"
    elif user_score > 21:
        return "You went over. You lose 🥲"
    elif computer_score > 21:
        return "Opponent went over. You win 🥳"
    elif user_score > computer_score:
        return "You win! 😊"
    else:
        return "You lose! 😒"
    
def play_game():
    """Play the game!"""
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score ==0 or user_score > 21:
            is_game_over = True
            print("Game over.")
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computers final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack type 'y' or 'n': ") == "y":
    clear()
    play_game()