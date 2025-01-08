first_rider_age = int(input('What is the age of the first rider? '))
first_rider_height = int(input("What is the height of the first rider? "))
have_second_rider = input("Is there a second rider (y/n)? ").lower() == 'y'

can_ride = False

if have_second_rider:
    second_rider_age = int(input("What is the age of the second rider? "))
    second_rider_height = int(input("What is the height of the second rider? "))

    if first_rider_age >= 18 and first_rider_height >= 36 and second_rider_height >= 36:
        can_ride = True
else:
    if first_rider_age >= 18 and first_rider_height >= 62:
        can_ride = True

if can_ride:
    print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Sorry, you may not ride.")
