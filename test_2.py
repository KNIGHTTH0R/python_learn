import unittest

def setUpModule():
    print("setUpModule() from test_2.py")

def tearDownModule():
    print("tearDownModule() from test_2.py")

class Test2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass() from Test2 class in test_2.py")

    
    def setUp(self):
        print("setUp() from Test2 in test_2.py")
    
    def test_simple(self):
        self.assertEqual(2+2,4)

    @unittest.skip("Skipping a test demo")
    def test_skip(self):
        self.fail("Never happens")

    def tearDown(self):
        print("tearDown() from Test2 in test_2.py")
    
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass() from Test2 class in test_2.py")


if __name__ == '__main__':
    unittest.main()