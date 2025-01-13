numbers = []

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    numbers.append(number)

print("The sum is: ", sum(numbers))
print("The average is: ", sum(numbers) / len(numbers))
print("The largest number is: ", max(numbers))
