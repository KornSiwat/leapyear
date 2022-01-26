from leapyear import is_leapyear, is_centuryyear

class TestLeapyearClass:
    def test_is_centuryyear_when_input_is_divisible_by_100(self):
        assert is_centuryyear(2000) == True

    def test_is_leapyear_when_input_is_centuryyear_divisible_by_400(self):
        assert is_leapyear(2000) == True