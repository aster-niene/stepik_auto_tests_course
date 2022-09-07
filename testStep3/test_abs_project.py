import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number")

    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

    def test_abs3(self):
        assert abs(-42) == 42, "Should be absolute value of a number"

    def test_abs4(self):
        assert abs(-42) == -42, "Should be absolute value of a number"
    def test_abs5(self):
        a = 4
        b = 5
        assert a == b, "Значения разные"


if __name__ == "__main__":
    unittest.main()