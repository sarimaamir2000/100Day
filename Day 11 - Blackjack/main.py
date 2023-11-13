import os # for clearing the screen when u wanna play blackjack again
import random
import art

# Make the inputs
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def hit(): # Get another card from deck if you want more points
    return your_card.append(cards[random.randint(0, len(cards) - 1)])
    
while go_again == "y":
    os.system('cls')
    print(art.logo)
    your_card = []
    dealer_card = []
    for i in range(0,2):
        your_card.append(cards[random.randint(0, len(cards) - 1)])
        dealer_card.append(cards[random.randint(0, len(cards) - 1)])

    print(f"Your cards are: {your_card[0]}, {your_card[1]}, current_score = {sum(your_card)}")
    print(f"Dealer's first card is: {dealer_card[0]}")

    hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
    while hit_me == "y" and sum(your_card) <= 21:
        hit()
        if sum(your_card) <= 21:
            print(f"Now your cards are: {your_card}, current score: {sum(your_card)}")
            print(f"Dealer's first card is: {dealer_card[0]}")
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ")
        else:
            break
        
        if sum(dealer_card) < 17:
            dealer_card.append(cards[random.randint(0, len(cards) - 1)])

    if hit_me == "n" or sum(your_card) > 21:
        print(f"Final: Your cards are: {your_card}, current_score = {sum(your_card)}")
        print(f"Final: Dealer's cards are: {dealer_card}, dealer_score = {sum(dealer_card)}")
        if sum(your_card) > 21:
            print("You busted! You lose.")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        elif sum(dealer_card) > sum(your_card) and (sum(dealer_card) <= 21):
            print("You lose!")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        elif (sum(your_card) == sum(dealer_card)):
            print("It's a draw!")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        elif (sum(your_card) > sum(dealer_card) and (sum(dealer_card) <= 21)):
            print("You win!")
            go_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


# if dealer card total is < 17, then keep getting another card until it passes the threshold

#figure out the while loop, where do they go for <21 or until you keep asking for another card

# if 'n' then decide who the winner is