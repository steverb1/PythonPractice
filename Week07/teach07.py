import random


magic_number = random.randint(1, 100)
guess = -1

while guess != magic_number:
    if guess < magic_number:
        print("Higher")
    elif guess > magic_number:
        print("Lower")
    guess = int(input("What is your guess? "))

print("You guessed it!")
