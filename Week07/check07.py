number = int(input("Please type a positive number: "))

while number < 0:
    print("Sorry, that is a negative number. Please try again.")
    number = int(input("Please type a positive number: "))

print("The number is: ", number)


answer = 'no'

while answer != 'yes':
    answer = input('May I have a piece of candy? ')

print('Thank you.')