"""
File: teach06_sample.py

Purpose: Amusement park ride requirements.
"""

def can_riders_ride(age1, height1, golden1, is_second_rider, age2 = None, height2 = None, golden2 = None):
    if is_second_rider:
        # Rule 1
        if height1 < 36 or height2 < 36:
            can_ride = False
        else:
            # Rule 3
            if age1 >= 18 or age2 >= 18 or golden1 or golden2:
                # At least one is an adult
                can_ride = True
            else:
                # Neither is an adult

                # Rule 4
                if age1 >= 12 and height1 >= 52 and age2 >= 12 and height2 >= 52:
                    can_ride = True
                elif (age1 >= 16 and age2 >= 14) or (age1 >= 14 and age2 >= 16):
                    # Rule 6
                    can_ride = True
                else:
                    can_ride = False
    else: # There is only one rider
        # Rule 2
        if (age1 >= 18 or golden1) and height1 >= 62:
            can_ride = True
        else:
            can_ride = False
    return can_ride

if __name__ == "__main__":
    # Notice the use of a boolean variable, set to False by default
    can_ride = False
    golden1 = None
    age2 = None
    height2 = None
    golden2 = None

    age1 = int(input("What is the age of the first rider? "))
    height1 = int(input("What is the height of the first rider? "))

    if age1 >= 12 and age1 < 18:
        golden1 = input("Does this rider have a golden passport (yes/no)? ")
        if golden1.lower() == 'yes':
            golden1 = True

    is_second_rider = input("Is there a second rider (yes/no)? ")
    if is_second_rider.lower() == "yes":
        is_second_rider = True
    else:
        is_second_rider = False

    if is_second_rider:
        age2 = int(input("What is the age of the second rider? "))
        height2 = int(input("What is the height of the second rider? "))

        if age2 >= 12 and age2 < 18:
            golden2 = input("Does this rider have a golden passport (yes/no)? ")
            if golden2.lower() == 'yes':
                golden2 = True

    can_ride = can_riders_ride(age1, height1, golden1, is_second_rider, age2, height2, golden2)

    if can_ride:
        print("Welcome to the ride. Please be safe and have fun!")
    else:
        print("Sorry, you may not ride.")
