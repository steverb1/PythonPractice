numbers = []

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    numbers.append(number)

print("The sum is: ", sum(numbers))
print("The average is: ", sum(numbers) / len(numbers))
print("The largest number is: ", max(numbers))

print("The smallest positive number is: ", min([x for x in numbers if x > 0]))

print("The sorted list is: ", sorted(numbers))
