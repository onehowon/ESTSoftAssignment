import unittest

def add(x,y):
    return x+y


def sub(x,y):
    return x- y

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        
    def test_sub(self):
        self.assertEqual(sub(10,2) 8)
        
if __name__ == "__main__":
    unittest.main()
    