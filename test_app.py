
import unittest
from app import add


class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(20, 30), 50)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)


if __name__ == "__main__":
    unittest.main()
