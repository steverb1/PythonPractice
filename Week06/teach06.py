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
            if rider1_height >= 52 and rider2_height >= 52:
                can_ride = True
    else:
        if rider1_age >= 18 and rider1_height >= 62:
            can_ride = True

    return can_ride
