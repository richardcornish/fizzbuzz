import unittest

from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fb = FizzBuzz()

    def test_fizz(self):
        self.assertEqual(self.fb.get_line(3), "Fizz")

    def test_buzz(self):
        self.assertEqual(self.fb.get_line(5), "Buzz")

    def test_fizzbuzz(self):
        self.assertEqual(self.fb.get_line(15), "FizzBuzz")

    def test_output(self):
        with open("tests/output.txt") as f:
            output = f.read()
            self.assertEqual(self.fb.get_output(), output)


if __name__ == "__main__":
    unittest.main()
