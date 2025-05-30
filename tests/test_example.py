import unittest


def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)


if __name__ == '__main__':
    unittest.main()
