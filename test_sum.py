from sum import sum


class TestSum:
    def test_additions_are_additive(self):
        assert sum(1, 1)  == 2, "expected two numbers to add up"