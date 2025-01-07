from check06 import determine_loan_approval


class Test_Check06:
    def test_check06_scenario1(self):
        approved = determine_loan_approval(8, 7, 8, 1)
        assert approved == True

    def test_check06_scenario2(self):
        approved = determine_loan_approval(5, 2, 7, 5)
        assert approved == True

    def test_check06_scenario3(self):
        approved = determine_loan_approval(8, 2, 8, 3)
        assert approved == False

    def test_check06_scenario4(self):
        approved = determine_loan_approval(2, 4, 1, 7)
        assert approved == True

    def test_check06_scenario5(self):
        approved = determine_loan_approval(4, 5, 5, 3)
        assert approved == False
