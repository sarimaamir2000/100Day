
import os
import art
auction_dictionary = [] # this is a list

flag = True
print(art.logo)
def add_new_bidder(name, bid):
    os.system('cls')
    new_person = {}
    new_person['Name'] = name
    new_person['Bid'] = bid
    auction_dictionary.append(new_person)

while flag:

    bidder_name = input("What is your name? ")
    bid_amount = int(input("How much would you like to bid? $"))
    go_again = input("Are there any other bidders? Type 'yes' or 'no'.")
    if go_again =='yes':
        add_new_bidder(bidder_name, bid_amount) # this adds the new bidder to the list as part of the dictionary
    else:
        flag = False

max_bid = 0
# winner_index = 0

for i in range(len(auction_dictionary)):
    if auction_dictionary[i]["Bid"] > max_bid:
        max_bid = auction_dictionary[i]["Bid"]
        winner_index = i

print(f"The winner is {auction_dictionary[winner_index]['Name']} with a bid of ${auction_dictionary[winner_index]['Bid']}")