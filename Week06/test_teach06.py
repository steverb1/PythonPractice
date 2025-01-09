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

    def test_stretch_rule1_not_18_can_ride(self):
        rider1_age = 17
        has_golden_passport1 = False
        rider1_height = 52
        have_second_rider = True
        rider2_age = 17
        rider2_height = 52
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age, rider2_height)
        assert can_ride == True

    def test_stretch_rule1_too_young_cannot_ride(self):
        rider1_age = 17
        has_golden_passport1 = False
        rider1_height = 52
        have_second_rider = True
        rider2_age = 11
        rider2_height = 52
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age, rider2_height)
        assert can_ride == False

    def test_stretch_rule1_too_short_cannot_ride(self):
        rider1_age = 17
        has_golden_passport1 = False
        rider1_height = 51
        have_second_rider = True
        rider2_age = 17
        rider2_height = 52
        has_goldern_passport2 = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age, rider2_height, has_goldern_passport2)
        assert can_ride == False

    def test_stretch_rule2_single_rider_too_short_cannot_ride(self):
        rider1_age = 12
        has_golden_passport1 = True
        rider1_height = 52
        have_second_rider = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider)
        assert can_ride == False

    def test_stretch_rule2_single_rider_tall_enough_can_ride(self):
        rider1_age = 12
        has_golden_passport1 = True
        rider1_height = 62
        have_second_rider = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider)
        assert can_ride == True

    def test_stretch_rule2_double_riders_can_ride(self):
        rider1_age = 17
        has_golden_passport1 = False
        rider1_height = 52
        have_second_rider = True
        rider2_age = 12
        rider2_height = 52
        has_golden_passport2 = True
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age, rider2_height, has_golden_passport2)
        assert can_ride == True

    # This is passing by accident. Without any guidance on height, stretch rule 3 is already covered by stretch rule 1.
    def test_stretch_rule3_double_riders_can_ride(self):
        rider1_age = 16
        has_golden_passport1 = False
        rider1_height = 52
        have_second_rider = True
        rider2_age = 14
        rider2_height = 52
        has_golden_passport2 = False
        can_ride = can_riders_ride(rider1_age, rider1_height, has_golden_passport1, have_second_rider, rider2_age, rider2_height, has_golden_passport2)
        assert can_ride == True
