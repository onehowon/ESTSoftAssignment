import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(10, 2), 13)
        self.assertEqual(add(10, 20), 31)


if __name__ == '__main__':
    unittest.main()