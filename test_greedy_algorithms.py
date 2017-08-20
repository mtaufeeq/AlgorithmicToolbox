import unittest
from greedy_algorithms import GreedyAlgorithms

class TestGreedyAlgorithms(unittest.TestCase):
    """ Unittest: IntroToAlgorithmicToolbox."""
    
    def test_get_change_example_1(self):
        """ Test get_change with 2."""
        money = GreedyAlgorithms()
        actual = money.get_change(2)
        expected = 2
        self.assertEqual(expected, actual)
        
    
    def test_get_change_example_2(self):
        """ Test get_change with 28."""
        money = GreedyAlgorithms()
        actual = money.get_change(28)
        expected = 6
        self.assertEqual(expected, actual)
        
        
    def test_get_optimal_value_of_fractional_knapsack_example_1(self):
        """ Test get_optimal_value_of_fractional_knapsack with 50, [20, 50, 30], [60, 100, 120]."""
        optimal = GreedyAlgorithms()
        actual = optimal.get_optimal_value_of_fractional_knapsack(50, [20, 50, 30], [60, 100, 120])
        expected = 180.0
        self.assertEqual(expected, actual)
        
    
    def test_get_optimal_value_of_fractional_knapsack_example_2(self):
        """ Test get_optimal_value_of_fractional_knapsack with 10, [30], [500]."""
        optimal = GreedyAlgorithms()
        actual = optimal.get_optimal_value_of_fractional_knapsack(10, [30], [500])
        expected = 166.6667
        self.assertEqual(expected, actual)
        
        
    def test_get_max_sum_of_dot_product_example_1(self):
        """ Test get_max_sum_of_dot_product with [23], [39]."""
        max_ = GreedyAlgorithms()
        actual = max_.get_max_sum_of_dot_product([23], [39])
        expected = 897
        self.assertEqual(expected, actual)
        
    
    def test_get_max_sum_of_dot_product_example_2(self):
        """ Test get_max_sum_of_dot_product with [1, 3, -5], [-2, 4, 1]."""
        max_ = GreedyAlgorithms()
        actual = max_.get_max_sum_of_dot_product([1, 3, -5], [-2, 4, 1])
        expected = 23
        self.assertEqual(expected, actual)
        
    
    def test_get_optimal_summands_example_1(self):
        """ Test get_optimal_summands with 8."""
        summands = GreedyAlgorithms()
        actual = summands.get_optimal_summands(8)
        expected = [1, 2, 5]
        self.assertEqual(expected, actual)
        
    
    def test_get_optimal_summands_example_2(self):
        """ Test get_optimal_summands with 2."""
        summands = GreedyAlgorithms()
        actual = summands.get_optimal_summands(2)
        expected = [2]
        self.assertEqual(expected, actual)
        
        
    def test_get_largest_number_example_1(self):
        """ Test get_largest_number with [58, 588]."""
        largest = GreedyAlgorithms()
        actual = largest.get_largest_number([58, 588])
        expected = '58858'
        self.assertEqual(expected, actual)
        
    
    def test_get_largest_number_example_2(self):
        """ Test get_largest_number with [21, 2]."""
        largest = GreedyAlgorithms()
        actual = largest.get_largest_number([21, 2])
        expected = '221'
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)