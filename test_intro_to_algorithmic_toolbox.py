import unittest
from intro_to_algorithmic_toolbox import IntroToAlgorithmicToolbox

class TestIntroToAlgorithmicToolbox(unittest.TestCase):
    """ Unittest: IntroToAlgorithmicToolbox."""
    
    
    def test_get_nth_fib_number_recur_example_1(self):
        """ Test get_nth_fib_number_recur with 0."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_nth_fib_number_recur(0)
        expected = 0
        self.assertEqual(expected, actual)
    
    
    def test_get_nth_fib_number_recur_example_2(self):
        """ Test get_nth_fib_number_recur with 10."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_nth_fib_number_recur(10)
        expected = 55
        self.assertEqual(expected, actual)

        
    def test_get_nth_fib_number_iter_example_1(self):
        """ Test test_get_nth_fib_number_iter with 0."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_nth_fib_number_iter(0)
        expected = 0
        self.assertEqual(expected, actual)
        
        
    def test_get_nth_fib_number_iter_example_2(self):
        """ Test test_get_nth_fib_number_iter with 10."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_nth_fib_number_iter(10)
        expected = 55
        self.assertEqual(expected, actual)
        
    def test_get_last_digit_of_fib_naive_example_1(self):
        """ Test get_fibonacci_last_digit_naive with 331."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_fib_naive(331)
        expected = 9
        self.assertEqual(expected, actual)
        
        
    def test_get_last_digit_of_fib_naive_example_2(self):
        """ Test get_fibonacci_last_digit_naive with 327305."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_fib_naive(327305)
        expected = 5
        self.assertEqual(expected, actual)
        
    
    def test_get_last_digit_of_fib_str_example_1(self):
        """ Test get_last_digit_of_fib_str with 331."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_fib_str(331)
        expected = 9
        self.assertEqual(expected, actual)
        
        
    def test_get_last_digit_of_fib_str_example_2(self):
        """ Test get_last_digit_of_fib_str with 3."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_fib_str(3)
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_last_digit_of_fib_fast_example_1(self):
        """ Test get_last_digit_of_fib_fast with 331."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_fib_fast(331)
        expected = 9
        self.assertEqual(expected, actual)
        
        
    def test_get_last_digit_of_fib_fast_example_2(self):
        """ Test get_last_digit_of_fib_fast with 327305."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_fib_fast(327305)
        expected = 5
        self.assertEqual(expected, actual)
        
        
    def test_gcd_naive_example_1(self):
        """ Test gcd_naive with 331."""
        number = IntroToAlgorithmicToolbox()
        actual = number.gcd_naive(18, 35)
        expected = 1
        self.assertEqual(expected, actual)
        
        
    def test_gcd_naive_example_2(self):
        """ Test gcd_naive with 327305."""
        number = IntroToAlgorithmicToolbox()
        actual = number.gcd_naive(25, 50)
        expected = 25
        self.assertEqual(expected, actual)
        
        
    def test_euclid_gcd_example_1(self):
        """ Test euclid_gcd with 18, 35."""
        number = IntroToAlgorithmicToolbox()
        actual = number.euclid_gcd(18, 35)
        expected = 1
        self.assertEqual(expected, actual)
        
        
    def test_euclid_gcd_example_2(self):
        """ Test euclid_gcd with 28851538, 1183019."""
        number = IntroToAlgorithmicToolbox()
        actual = number.euclid_gcd(28851538, 1183019)
        expected = 17657
        self.assertEqual(expected, actual)
        
    
    def test_lcm_naive_example_1(self):
        """ Test lcm_naive with 6, 8."""
        number = IntroToAlgorithmicToolbox()
        actual = number.lcm_naive(6, 8)
        expected = 24
        self.assertEqual(expected, actual)
        
        
    def test_lcm_naive_example_2(self):
        """ Test euclid_gcd with 6, 8."""
        number = IntroToAlgorithmicToolbox()
        actual = number.lcm_naive(6, 8)
        expected = 17657
        self.assertEqual(expected, actual)
        
        
    def test_lcm_euclid_gcd_example_1(self):
        """ Test lcm_euclid_gcd with 6, 8."""
        number = IntroToAlgorithmicToolbox()
        actual = number.lcm_euclid_gcd(6, 8)
        expected = 24
        self.assertEqual(expected, actual)
        
        
    def test_lcm_euclid_gcd_example_2(self):
        """ Test lcm_euclid_gcd with 28851538, 1183019."""
        number = IntroToAlgorithmicToolbox()
        actual = number.lcm_euclid_gcd(28851538, 1183019)
        expected = 1933053046
        self.assertEqual(expected, actual)
        
        
    def test_get_fibonacci_huge_mod_m_naive_example_1(self):
        """ Test get_fibonacci_huge_mod_m_naive with 1, 239."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_fibonacci_huge_mod_m_naive(1, 239)
        expected = 1
        self.assertEqual(expected, actual)
        
        
    def test_get_fibonacci_huge_mod_m_naive_example_2(self):
        """ Test get_fibonacci_huge_mod_m_naive with 239, 1000."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_fibonacci_huge_mod_m_naive(239, 1000)
        expected = 161
        self.assertEqual(expected, actual)
        
    
    def test_get_pisano_period_example_1(self):
        """ Test get_pisano_period with 5."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_pisano_period(5)
        expected = 20
        self.assertEqual(expected, actual)
        
        
    def test_get_pisano_period_example_2(self):
        """ Test get_pisano_period with 9."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_pisano_period(9)
        expected = 24
        self.assertEqual(expected, actual)
        
    
    def test_get_fibonacci_huge_mod_m_fast_example_1(self):
        """ Test get_fibonacci_huge_mod_m_fast with 1, 239."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_fibonacci_huge_mod_m_fast(1, 239)
        expected = 1
        self.assertEqual(expected, actual)
        
        
    def test_get_fibonacci_huge_mod_m_fast_example_2(self):
        """ Test get_fibonacci_huge_mod_m_fast with 239, 1000."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_fibonacci_huge_mod_m_fast(239, 1000)
        expected = 161
        self.assertEqual(expected, actual)
        
        
    def test_get_mod_of_sum_of_last_fib_digits_naive_example_1(self):
        """ Test get_mod_of_sum_of_last_fib_digits_naive with 3."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_mod_of_sum_of_last_fib_digits_naive(3)
        expected = 4
        self.assertEqual(expected, actual)
        
        
    def test_get_mod_of_sum_of_last_fib_digits_naive_example_2(self):
        """ Test get_mod_of_sum_of_last_fib_digits_naive with 100."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_mod_of_sum_of_last_fib_digits_naive(100)
        expected = 5
        self.assertEqual(expected, actual)
        
    def test_get_last_digit_of_sum_of_fibonacci_numbers_example_1(self):
        """ Test get_last_digit_of_sum_of_fibonacci_numbers with 3."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_sum_of_fibonacci_numbers(3)
        expected = 4
        self.assertEqual(expected, actual)
        
        
    def test_get_last_digit_of_sum_of_fibonacci_numbers_example_2(self):
        """ Test get_last_digit_of_sum_of_fibonacci_numbers with 100."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_last_digit_of_sum_of_fibonacci_numbers(100)
        expected = 5
        self.assertEqual(expected, actual)
        
    
    def test_fibonacci_mod_of_partial_sum_naive_example_1(self):
        """ Test fibonacci_mod_of_partial_sum_naive with 3, 7."""
        number = IntroToAlgorithmicToolbox()
        actual = number.fibonacci_mod_of_partial_sum_naive(3, 7)
        expected = 1
        self.assertEqual(expected, actual)
        
        
    def test_fibonacci_mod_of_partial_sum_naive_example_2(self):
        """ Test fibonacci_mod_of_partial_sum_naive with 10, 200."""
        number = IntroToAlgorithmicToolbox()
        actual = number.fibonacci_mod_of_partial_sum_naive(10, 200)
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_mod_of_sum_of_last_digits_partial_example_1(self):
        """ Test get_mod_of_sum_of_last_digits_partial with 3, 7."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_mod_of_sum_of_last_digits_partial(3, 7)
        expected = 1
        self.assertEqual(expected, actual)
        
        
    def test_get_mod_of_sum_of_last_digits_partial_example_2(self):
        """ Test get_mod_of_sum_of_last_digits_partial with 10, 200."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_mod_of_sum_of_last_digits_partial(10, 200)
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_partial_sum_of_fibonacci_series_example_1(self):
        """ Test get_partial_sum_of_fibonacci_series with 3, 7."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_partial_sum_of_fibonacci_series(3, 7)
        expected = 1
        self.assertEqual(expected, actual)
        
        
    def test_get_partial_sum_of_fibonacci_series_example_2(self):
        """ Test get_partial_sum_of_fibonacci_series with 1234, 12345."""
        number = IntroToAlgorithmicToolbox()
        actual = number.get_partial_sum_of_fibonacci_series(1234, 12345)
        expected = 8
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
