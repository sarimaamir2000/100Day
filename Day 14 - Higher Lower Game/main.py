import random
import os
import art
import game_data

def get_random():
    newdata = random.choice(game_data.data)
    #return f"Compare B: {newdata['name']} a {newdata['description']}, from {newdata['country']}"
    return newdata


def game():
    global random_element1, random_element2, score, flag
    print(art.logo)
    if flag:
        print(f"You are correct! Current score: {score}")
    print(f"Compare A: {random_element1['name']} a {random_element1['description']}, from {random_element1['country']}")
    print(art.vs)
    print(f"Compare B: {random_element2['name']} a {random_element2['description']}, from {random_element2['country']}")

    user_input = input("Who do you think has more followers? Type 'A' or 'B': ").lower()
   
    if user_input == 'a' and random_element1['follower_count'] > random_element2['follower_count']:
        os.system('cls')
        score += 1
        flag = True
        random_element1 = random_element2
        random_element2 = get_random()
        game()
    elif user_input == 'b' and random_element1['follower_count'] < random_element2['follower_count']:
        os.system('cls')
        score += 1
        flag = True
        random_element1 = random_element2
        random_element2 = get_random() 
        game()
    else:
        os.system('cls')
        print(art.logo)
        print(f"That was incorrect! You lost. Final score {score}")          
        return

random_element1 = get_random()
random_element2 = get_random()
flag = False
score = 0
game()







