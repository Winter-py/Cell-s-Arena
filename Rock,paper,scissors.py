#Rock, paper, scissors
import random
while True:
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

    if user_input == "Paper":
        if random.hand == "Scissors":
            print("You lose!", random.hand, "cut", user_input)
        else:
            print("You win!", user_input, "covers", random.hand)

    if user_input == "Scissors":
        if random.hand == "Rock":
            print("You lose...", random.hand, "smashes", user_input)
        else:
            print("You win!", user_input, "cut", random.hand)

    play_again = input("Play again? Y/N ")
    if play_again == "Y" or "y":
        print("Let's play!")
    else:
        print("Thanks for playing!")
        break