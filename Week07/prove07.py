secret_word = "apple"
num_guesses = 1
guess = ""

print("Welcome to the word guessing game!")
print()

guess = input("What is your guess? ")

while guess != secret_word:
    print("Your guess was not correct.")
    guess = input("What is your guess? ")
    num_guesses += 1

print("Congratulations! You guessed it!")
print(f"It took you {num_guesses} guesses!")
