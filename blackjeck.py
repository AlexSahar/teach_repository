import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(list):
    if  sum(list) == 21 and len(list) == 2:
        return 0
    elif 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    return sum(list)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 🙄"

    if user_score == computer_score:
        return "Draw 😉"
    elif computer_score == 0:
        return "Lose, opponent has Blackjeck 😨"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Computer went over. You win 😃"
    elif user_score > computer_score:
        return "You wins 😊"
    else:
        return "You lose 🤧"

def play_game():

    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"{user_cards} and {user_score}")
        print(f"{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}. final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}. final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want play a game of Blackjack? 'y' or 'n' ") == 'y':
    play_game()
