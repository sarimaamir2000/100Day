import os # for clearing the screen when u wanna play blackjack again
import random
import art

# Make the inputs
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def hit(): # Get another card from deck if you want more points
    return your_card.append(cards[random.randint(0, len(cards) - 1)])

def calculate_score(cards):
    ace_count = cards.count(11)
    if ace_count == 1 and sum(cards) > 21:
        ace_index = cards.index(11)
        cards[ace_index] = 1
        return sum(cards)
    else:
        return sum(cards)

        

while go_again == "y":
    os.system('cls')
    print(art.logo)
    your_card = []
    dealer_card = []
    for i in range(0,2):
        your_card.append(cards[random.randint(0, len(cards) - 1)])
        dealer_card.append(cards[random.randint(0, len(cards) - 1)])

    print(f"Your cards are: {your_card[0]}, {your_card[1]}, current_score = {calculate_score(your_card)}")
    print(f"Dealer's first card is: {dealer_card[0]}")

    hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
    while hit_me == "y" and calculate_score(your_card) <= 21:
        hit()
        if calculate_score(your_card) <= 21:
            print(f"Now your cards are: {your_card}, current score: {calculate_score(your_card)}")
            print(f"Dealer's first card is: {dealer_card[0]}")
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            break

        if calculate_score(dealer_card) < 16:
            dealer_card.append(cards[random.randint(0, len(cards) - 1)])

    if hit_me == "n" or calculate_score(your_card) > 21:
        print(f"Final: Your cards are: {your_card}, current_score = {calculate_score(your_card)}")
        print(f"Final: Dealer's cards are: {dealer_card}, dealer_score = {calculate_score(dealer_card)}")
        if calculate_score(your_card) > 21:
            print("You busted! You lose.")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        elif calculate_score(dealer_card) > calculate_score(your_card) and (calculate_score(dealer_card) <= 21):
            print("You lose!")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        elif (calculate_score(your_card) == calculate_score(dealer_card)):
            print("It's a draw!")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        elif (calculate_score(your_card) > calculate_score(dealer_card) and (calculate_score(dealer_card) <= 21)):
            print("You win!")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

