def can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age = None, rider2_height = None, has_golden_passport2 = None):
    if has_golden_passport1:
        rider1_age = 18

    can_ride = False

    if have_second_rider:
        if has_golden_passport2:
            rider2_age = 18

        if rider1_height < 36 or rider2_height < 36:
            can_ride = False
        elif rider1_age >= 18 and rider1_height >= 36 and rider2_height >= 36:
            can_ride = True
        elif rider1_age >= 12 and rider2_age >= 12 and rider1_height >= 52 and rider2_height >= 52:
            can_ride = True
        elif (rider1_age >= 16 and rider2_age >= 14) or (rider1_age >= 14 and rider2_age >= 16):
            if rider1_height >= 36 and rider2_height >= 36:
                can_ride = True
    else:
        if rider1_age >= 18 and rider1_height >= 62:
            can_ride = True

    return can_ride

if __name__ == "__main__":
    has_golden_passport1 = False
    second_rider_age = None
    second_rider_height = None
    has_golden_passport2 = False

    first_rider_age = int(input('What is the age of the first rider? '))
    if first_rider_age >= 12 and first_rider_age <= 17:
        has_golden_passport1 = input('Do you have a golden passport (y/n)? ').lower() == 'y'
    first_rider_height = int(input("What is the height of the first rider? "))

    have_second_rider = input("Is there a second rider (y/n)? ").lower() == 'y'
    if have_second_rider:
        second_rider_age = int(input("What is the age of the second rider? "))
        if second_rider_age >= 12 and second_rider_age <= 17:
            has_golden_passport2 = input('Do you have a golden passport (y/n)? ').lower() == 'y'
        second_rider_height = int(input("What is the height of the second rider? "))

    can_ride = can_riders_ride(first_rider_age, first_rider_height, has_golden_passport1, have_second_rider, second_rider_age, second_rider_height, has_golden_passport2)

    if can_ride:
        print("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry, you may not ride.")
