from teach06 import can_riders_ride

class Test_Teach06:

    def test_rule1_short_single_rider_cannot_ride(self):
        rider1_age = 18
        has_golden_passport1 = False
        rider1_height = 35
        have_second_rider = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider)
        assert can_ride == False

    def test_rule1_short_double_rider_cannot_ride(self):
        rider1_age = 18
        has_golden_passport1 = False
        rider1_height = 62
        have_second_rider = True
        rider2_age = 18
        rider2_height = 35
        has_golden_passport2 = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age, rider2_height, has_golden_passport2)
        assert can_ride == False

    def test_rule2_short_single_rider_cannot_ride(self):
        rider1_age = 18
        has_golden_passport1 = False
        rider1_height = 61
        have_second_rider = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider)
        assert can_ride == False

    def test_rule2_young_single_rider_cannot_ride(self):
        rider1_age = 17
        has_golden_passport1 = False
        rider1_height = 62
        have_second_rider = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider)
        assert can_ride == False

    def test_rule2_single_rider_can_ride(self):
        rider1_age = 18
        has_golden_passport1 = False
        rider1_height = 62
        have_second_rider = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider)
        assert can_ride == True

    def test_rule3_two_riders_one_18_can_ride(self):
        rider1_age = 18
        has_golden_passport1 = False
        rider1_height = 52
        have_second_rider = True
        rider2_age = 17
        rider2_height = 52
        has_golden_passport2 = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age, rider2_height, has_golden_passport2)
        assert can_ride == True
