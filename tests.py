import unittest

def setUpModule():
    print("setUpModule() from tests.py")

def tearDownModule():
    print("tearDownModule() from tests.py")

def division(x,y):
    """Return result of division"""
    try:
        return x/y
    except ZeroDivisionError:
        print("Division by zero")

class Testexceptions(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass() from Testexceptions class in tests.py")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass() from Testexceptions class in tests.py")

    def setUp(self):
        print("setUp() from Testexceptions in tests.py")
    def tearDown(self):
        print("tearDown() from Testexceptions in tests.py")
    
    def test_basic(self):
        self.assertEqual(division(10,5), 2.0)
        self.assertEqual(division(10,-2), -5.0)

    def test_type_exceptions(self):
        with self.assertRaises(TypeError):
            division(10,'a')
    
    def test_zero_division(self):
        try:
            division(10,0)
        except ZeroDivisionError:
            self.fail("ZeroDivisionError")

if __name__ == '__main__':
    unittest.main()