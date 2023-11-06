rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rps = [rock , paper, scissors]
num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

user = rps[num]
computer = random.choice(rps)

if user == computer:
  print(f"You chose {user} and the computer chose {computer} It's a tie!")
elif user == rock and computer == scissors:
   print(f"You chose {user} and the computer chose {computer} You win!")
elif user == rock and computer == paper:
   print(f"You chose {user} and the computer chose {computer} You lose.")
elif user == paper and computer == rock:
   print(f"You chose {user} and the computer chose {computer} You win!")
elif user == paper and computer == scissors:
   print(f"You chose {user} and the computer chose {computer} You lose!")
elif user == scissors and computer == rock:
   print(f"You chose {user} and the computer chose {computer} You lose!")
elif user == scissors and computer == paper:
   print(f"You chose\n {user}\n and the computer chose {computer}\n You win!")





