import random

play_again = 'yes'

while play_again == 'yes':
    magic_number = random.randint(1, 100)
    guess = -1
    number_of_guesses = 0

    while guess != magic_number:
        guess = int(input("What is your guess? "))
        if guess < magic_number:
            print("Higher")
        elif guess > magic_number:
            print("Lower")
        number_of_guesses += 1
        
    print(f"You guessed it in {number_of_guesses} guesses!")

    play_again = input("Do you want to play again? ")
