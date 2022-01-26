from leapyear import is_leapyear, is_centuryyear

class TestLeapyearClass:
    def test_is_centuryyear_when_input_is_divisible_by_100(self):
        assert is_centuryyear(2000) == True