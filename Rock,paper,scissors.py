#Rock, paper, scissors
import random

hands = ["Rock", "Paper", "Scissors"]

user_input = input("Rock, paper, scissors? ")

random.hand = random.choice(hands)

if user_input == random.hand:
    print("It's a tie!")
elif user_input == "Rock":
    if random.hand == "Paper":
        print("You lose!", random.hand, "covers", user_input)
    else:
        print("You win!", user_input, "smashes", random.hand)