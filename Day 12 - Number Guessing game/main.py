import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

input_user = input("Choose a difficulty. Type 'easy' or 'hard': ")
random_number  = random.randint(1, 100)
#print(f"Psst. The number is {random_number}") uncomment this if you want to find out the actual number


def guessing(num_guess):
    flag = False
    while num_guess > 0:
        guess = int(input("Guess a number: "))
        if guess == random_number:
            print("Congratulations! You got it right.")
            flag = True
            break
        elif guess < random_number:
            print(f"Too low! Try again...\nYou have {num_guess - 1} guesses left")
        else:
            print(f"Too high! Try again...\nYou have {num_guess - 1} guesses left")

        num_guess -= 1

    if not flag:
        print(f"Game over! The correct answer was {random_number}")


if input_user == "easy":
    print("You have 10 guesses")
    guessing(10)
elif input_user == "hard":
    print("You have 5 guesses")
    guessing(5)
