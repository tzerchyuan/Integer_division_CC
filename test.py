import unittest
from solution import solution

class Test(unittest.TestCase):
    '''
    testing strategy
        partition space:
            abs(numerator) = abs(denominator)
                numerator > 0 , denominator > 0
                numerator < 0 , denominator > 0
                numerator < 0 , denominator < 0
                numerator > 0 , denominator < 0
            numerator > denominator:
                numerator > 0 , denominator > 0
                numerator > 0 , denominator < 0
                numerator < 0 , denominator < 0
            numerator < denominator:
                numerator < 0 , denominator > 0
                numerator < 0 , denominator < 0
                numerator > 0 , denominator > 0
            edge cases:
                numerator = 0 , denominator > 0
                numerator = 0 , denominator < 0
                numerator > 0 , denominator = 0
                numerator < 0 , denominator = 0
    '''
    def test_num_equal_1(self):
        """
        abs(numerator) = abs(denominator)
        numerator > 0 , denominator > 0
        """
        self.assertEqual(solution(5, 5)[0], divmod(5, 5)[0])
        self.assertEqual(solution(5, 5)[1], divmod(5, 5)[1])

    def test_num_equal_2(self):
        """
        abs(numerator) = abs(denominator)
        numerator > 0 , denominator < 0
        """
        self.assertEqual(solution(5, -5)[0], divmod(5, -5)[0])
        self.assertEqual(solution(5, -5)[1], divmod(5, -5)[1])

    def test_num_equal_3(self):
        """
        abs(numerator) = abs(denominator)
        numerator < 0 , denominator > 0
        """
        self.assertEqual(solution(-5, 5)[0], divmod(-5, 5)[0])
        self.assertEqual(solution(-5, 5)[1], divmod(-5, 5)[1])

    def test_num_equal_4(self):
        """
        abs(numerator) = abs(denominator)
        numerator < 0 , denominator < 0
        """
        self.assertEqual(solution(-5, -5)[0], divmod(-5, -5)[0])
        self.assertEqual(solution(-5, -5)[1], divmod(-5, -5)[1])

    def test_num_pos_denom_pos(self):
        """
        numerator > denominator
        numerator > 0 , denominator > 0
        """
        self.assertEqual(solution(6, 5)[0], divmod(6, 5)[0])
        self.assertEqual(solution(6, 5)[1], divmod(6, 5)[1])

    def test_num_pos_denom_neg(self):
        """
        numerator > denominator
        numerator > 0 , denominator < 0
        """
        self.assertEqual(solution(6, -5)[0], divmod(6, -5)[0])
        self.assertEqual(solution(6, -5)[1], divmod(6, -5)[1])

    def test_num_larger_denom_both_neg(self):
        """
        numerator > denominator
        numerator < 0 , denominator < 0
        """
        self.assertEqual(solution(-2, -7)[0], divmod(-2, -7)[0])
        self.assertEqual(solution(-2, -7)[1], divmod(-2, -7)[1])

    def test_num_neg_denom_pos(self):
        """
        numerator < denominator
        numerator < 0 , denominator > 0
        """
        self.assertEqual(solution(-6, 5)[0], divmod(-6, 5)[0])
        self.assertEqual(solution(-6, 5)[1], divmod(-6, 5)[1])

    def test_num_neg_denom_neg(self):
        """
        numerator < denominator
        numerator < 0 , denominator < 0
        """
        self.assertEqual(solution(-6, -5)[0], divmod(-6, -5)[0])
        self.assertEqual(solution(-6, -5)[1], divmod(-6, -5)[1])

    def test_num_smaller_denom_both_pos(self):
        """
        numerator < denominator
        numerator > 0 , denominator > 0
        """
        self.assertEqual(solution(5, 7)[0], divmod(5, 7)[0])
        self.assertEqual(solution(5, 7)[1], divmod(5, 7)[1])

    def test_num_zero_denom_pos(self):
        """
        edge case
        numerator = 0 , denominator > 0
        """
        self.assertEqual(solution(0, 5)[0], divmod(0, 5)[0])
        self.assertEqual(solution(0, 5)[1], divmod(0, 5)[1])

    def test_num_zero_denom_neg(self):
        """
        edge case
        numerator = 0 , denominator < 0
        """
        self.assertEqual(solution(0, -5)[0], divmod(0, -5)[0])
        self.assertEqual(solution(0, -5)[1], divmod(0, -5)[1])

    def test_num_pos_denom_zero(self):
        """
        edge case
        numerator > 0 , denominator = 0
        """
        try:
            solution(6, 0)
        except ArithmeticError:
            self.assertTrue(True)

    def test_num_neg_denom_zero(self):
        """
        edge case
        numerator > 0 , denominator = 0
        """
        try:
            solution(-5, 0)
        except ArithmeticError:
            self.assertTrue(True)

if __name__ == '__main__':

    #Prompt user for values, uncomment for debugging

    num = int(raw_input("Please enter numerator: "))
    denom = int(raw_input("Please enter denominator: "))
    try:
        print "%s / %s: quotient = %s" % (num, denom, solution(num, \
        denom)[0])
        print "%s / %s: remainder = %s" % (num, denom, solution(num, denom)[1])
    except ArithmeticError:
        print "Denominator cannot be zero!"


    #Running test cases
    unittest.main()
