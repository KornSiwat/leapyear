from leapyear import is_leapyear, is_centuryyear

class TestLeapyearClass:
    def test_is_centuryyear_when_input_is_divisible_by_100(self):
        assert is_centuryyear(2000) == True

    def test_is_leapyear_when_input_is_centuryyear_divisible_by_400(self):
        assert is_leapyear(2000) == True

    def test_is_not_centuryyear_when_input_is_not_divisible_by_100(self):
        assert is_centuryyear(2022) == False

    def test_is_leapyear_when_input_is_divisible_by_4(self):
        assert is_leapyear(2092) == True

    def test_is_not_leapyear_when_input_centuryyear_not_divisble_by_400_and_not_centuryyear_not_divisible_by_4(self):
        assert is_leapyear(1999) == False