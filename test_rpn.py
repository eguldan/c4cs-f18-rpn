import unittest
import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    
    def test_sub(self):
        result = rpn.calculate('4 3 -')
        self.assertEqual(1, result)

    def test_toomany(self):
        with  self.assertRaises(ValueError):
            result = rpn.calculate('1 2 3 +')
 
    def test_exponent(self):
        result = rpn.calculate('4 3 ^')
        self.assertEqual(64, result)


    def test_additionalKeys(self):
        result = rpn.calculate('72 5 %')
        self.assertEqual(3.6, result)
        result2 = rpn.calculate('3 4 ^')
        self.assertEqual(81, result2)
        result3 = rpn.calculate('10 3 //')
        self.assertEqual(3, result3)
    
    def test_summation(self):
        result = rpn.calculate('5 10 15 20 25 sum')
        self.assertEqual(75, result)

    def test_factorial(self):
        result = rpn.calculate('4 !')
        self.assertEqual(24, result)



