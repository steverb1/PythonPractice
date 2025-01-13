sentence = 'The quick brown fox jumps over the lazy dog'
run_again = True

while run_again:
    number = int(input('Please enter a number: '))

    for i, letter in enumerate(sentence):
        if i % number == 0:
            print(letter.upper(), end = '')
        else:
            print(letter, end = '')
    print()

    run_again = input('Would you like to enter another number? ').lower() == 'yes'

print('Goodbye!')
