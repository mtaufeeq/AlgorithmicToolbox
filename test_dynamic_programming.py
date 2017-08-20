import unittest
from dynamic_programming import DynamicProgramming

class TestDynamicProgramming(unittest.TestCase):
    """ Unit test: divide and conquer. """
    
    def test_get_optimal_weight_knapsack_with_no_rep_example_1(self):
        """ Test get_optimal_weight_knapsack_with_no_rep with 10, [1, 4, 8]."""
        optimal_weight = DynamicProgramming()
        actual = optimal_weight.get_optimal_weight_knapsack_with_no_rep(10, [1, 4, 8])
        expected = 9
        self.assertEqual(expected, actual)
        
        
    def test_get_optimal_weight_knapsack_with_no_rep_example_2(self):
        """ Test get_optimal_weight_knapsack_with_no_rep with 10, [3, 6, 4, 2]."""
        optimal_weight = DynamicProgramming()
        actual = optimal_weight.get_optimal_weight_knapsack_with_no_rep(10, [3, 6, 4, 2])
        expected = 10
        self.assertEqual(expected, actual)
        
        
    def test_get_edit_distance_example_1(self):
        """ Test get_edit_distance with 'ab' 'ab'."""
        edit_dist = DynamicProgramming()
        actual = edit_dist.get_edit_distance('ab', 'ab')
        expected = 0
        self.assertEqual(expected, actual)
        
        
    def test_get_edit_distance_example_2(self):
        """ Test get_edit_distance with 'editing', 'distance'."""
        edit_dist = DynamicProgramming()
        actual = edit_dist.get_edit_distance('editing', 'distance')
        expected = 5
        self.assertEqual(expected, actual)
        
        
    def test_get_max_val_of_arith_expr_via_parentheses_example_1(self):
        """ Test get_max_val_of_arith_expr_via_parentheses with '1+2-3*4-5'."""
        max_val_of_arith_expr = DynamicProgramming()
        actual = max_val_of_arith_expr.get_max_val_of_arith_expr_via_parentheses('1+2-3*4-5')
        expected = 6
        self.assertEqual(expected, actual)
        
        
    def test_get_max_val_of_arith_expr_via_parentheses_example_2(self):
        """ Test get_max_val_of_arith_expr_via_parentheses with '5-8+7*4-8+9'."""
        max_val_of_arith_expr = DynamicProgramming()
        actual = max_val_of_arith_expr.get_max_val_of_arith_expr_via_parentheses('5-8+7*4-8+9')
        expected = 200
        self.assertEqual(expected, actual)
        
        
    def test_get_longest_common_subsequence_3_example_1(self):
        """ Test get_longest_common_subsequence_3 with [1, 2, 3], [1, 3, 2], [2, 1, 3]."""
        lcs_3 = DynamicProgramming()
        actual = lcs_3.get_longest_common_subsequence_3([1, 2, 3], [1, 3, 2], [2, 1, 3])
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_longest_common_subsequence_3_example_2(self):
        """ Test get_longest_common_subsequence_3 with [8, 3, 2, 1, 7], 
                                                        [8, 2, 1, 3, 8, 10, 7],
                                                        [6, 8, 3, 1, 4, 7]."""
        lcs_3 = DynamicProgramming()
        actual = lcs_3.get_longest_common_subsequence_3([8, 3, 2, 1, 7], 
                                                        [8, 2, 1, 3, 8, 10, 7],
                                                        [6, 8, 3, 1, 4, 7])
        expected = 3
        self.assertEqual(expected, actual)
        
        
if __name__ == '__main__':
    unittest.main(exit=False)
        