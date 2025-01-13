secret = "apple"
num_guesses = 0
guess = ""

print("Welcome to the word guessing game!")
print()

secret_length = len(secret)
print('Your hint is: ', end="")
for i in range(secret_length):
    print("_", end=" ")
print()

while guess != secret:
    guess = input("What is your guess? ").lower()
    num_guesses += 1
    if guess == secret:
        break
    if len(guess) != len(secret):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        print("Your hint is: ", end="")
        for i in range(secret_length):
            if guess[i] == secret[i]:
                print(guess[i].upper(), end=" ")
            elif guess[i] in secret:
                print(guess[i], end=" ")
            else:
                print("_", end=" ")
        print()

print("Congratulations! You guessed it!")
print(f"It took you {num_guesses} guesses.")
