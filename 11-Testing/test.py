import unittest 
import main # Use all func available in main

class TestMain(unittest.TestCase): # Inherit what unit test gives us (TestCase)
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param) 
        self.assertEqual(result, 15) #assert equal tests the two paramsr equal
    
    def test_do_stuff_2(self):
        test_param = "testing"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError) # This will pass as it returns True, resut is an instance of a valueError

    def test_do_stuff_3(self):
        test_param = None 
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")
    
    def test_do_stuff_4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

if __name__ == '__main__': # ensure only run if its main file 
    # to run all test.py (because there shoul b more test for ev module. run python -m unittest)
    # attach v flag for more detail
    unittest.main() # This returns ok as 10 + 5 = 15, if i said 10 instead of 15 it would fail


# Look at unittest for more methods
# Best to repeat urself for test so they r easy to read. DRY is less a priority