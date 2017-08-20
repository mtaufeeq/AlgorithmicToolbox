import unittest
from divide_and_conquer import DivideAndConquer

class TestDivideAndConquer(unittest.TestCase):
    """ Unit test: divide and conquer. """
    
    def test_linear_search_example_1(self):
        """ Test linear_search with [5, 8, 1, 23, 1, 10], 23."""
        key_val = DivideAndConquer()
        actual = key_val.linear_search([5, 8, 1, 23, 1, 10], 23)
        expected = 3
        self.assertEqual(expected, actual)
        
        
    def test_linear_search_example_2(self):
        """ Test linear_search with [5, 8, 1, 23, 1, 10], 100."""
        key_val = DivideAndConquer()
        actual = key_val.linear_search([5, 8, 1, 23, 1, 10], 100)
        expected = -1
        self.assertEqual(expected, actual)
        
        
    def test_binary_search_example_1(self):
        """ Test binary_search with [5, 8, 1, 23, 1, 10], 23."""
        key_val = DivideAndConquer()
        actual = key_val.binary_search([5, 8, 1, 23, 1, 10], 23)
        expected = 5
        self.assertEqual(expected, actual)
        
        
    def test_binary_search_example_2(self):
        """ Test binary_search with [5, 8, 1, 23, 1, 10], 100."""
        key_val = DivideAndConquer()
        actual = key_val.binary_search([5, 8, 1, 23, 1, 10], 100)
        expected = -1
        self.assertEqual(expected, actual)
        
        
    def test_get_majority_element_naive_example_1(self):
        """ Test get_majority_element_naive with [2, 3, 9, 2, 2], 0, len([2, 3, 9, 2, 2]."""
        maj_elm = DivideAndConquer()
        actual = maj_elm.get_majority_element_naive([2, 3, 9, 2, 2], 0, len([2, 3, 9, 2, 2]))
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_majority_element_naive_example_2(self):
        """ Test get_majority_element_naive with [1, 2, 3, 4], 0, len([1, 2, 3, 4]."""
        maj_elm = DivideAndConquer()
        actual = maj_elm.get_majority_element_naive([1, 2, 3, 4], 0, len([1, 2, 3, 4]))
        expected = -1
        self.assertEqual(expected, actual)
        
        
    def test_get_majority_element_sort_count_example_1(self):
        """ Test get_majority_element_sort_count with [2, 3, 9, 2, 2], 0, len([2, 3, 9, 2, 2]."""
        maj_elm = DivideAndConquer()
        actual = maj_elm.get_majority_element_sort_count([2, 3, 9, 2, 2], 0, len([2, 3, 9, 2, 2]))
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_majority_element_sort_count_example_2(self):
        """ Test get_majority_element_sort_count with [1, 2, 3, 4], 0, len([1, 2, 3, 4]."""
        maj_elm = DivideAndConquer()
        actual = maj_elm.get_majority_element_sort_count([1, 2, 3, 4], 0, len([1, 2, 3, 4]))
        expected = -1
        self.assertEqual(expected, actual)
        
        
    def test_get_majority_element_linear_example_1(self):
        """ Test get_majority_element_linear with [2, 3, 9, 2, 2]."""
        maj_elm = DivideAndConquer()
        actual = maj_elm.get_majority_element_linear([2, 3, 9, 2, 2])
        expected = 3
        self.assertEqual(expected, actual)
        
        
    def test_get_majority_element_linear_example_2(self):
        """ Test get_majority_element_linear with [2, 2, 2, 2, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0]."""
        maj_elm = DivideAndConquer()
        actual = maj_elm.get_majority_element_linear([2, 2, 2, 2, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0])
        expected = 9
        self.assertEqual(expected, actual)
        
        
    def test_randomized_quick_sort_2_way_p_example_1(self):
        """ Test randomized_quick_sort_2_way_p with [4, 2, 3, 4, 1], 0, 4."""
        list_ = DivideAndConquer()
        actual = list_.randomized_quick_sort_2_way_p([4, 2, 3, 4, 1], 0, 4)
        expected = [1, 2, 3, 4, 4]
        self.assertEqual(expected, actual)
        
        
    def test_randomized_quick_sort_2_way_p_example_2(self):
        """ Test randomized_quick_sort_2_way_p with [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9."""
        list_ = DivideAndConquer()
        actual = list_.randomized_quick_sort_2_way_p([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expected, actual)
        
        
    def test_randomized_quick_sort_3_way_p_example_1(self):
        """ Test randomized_quick_sort_3_way_p with [4, 2, 3, 4, 1], 0, 4."""
        list_ = DivideAndConquer()
        actual = list_.randomized_quick_sort_3_way_p([4, 2, 3, 4, 1], 0, 4)
        expected = [1, 2, 3, 4, 4]
        self.assertEqual(expected, actual)
        
        
    def test_randomized_quick_sort_3_way_p_example_2(self):
        """ Test randomized_quick_sort_3_way_p with [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9."""
        list_ = DivideAndConquer()
        actual = list_.randomized_quick_sort_3_way_p([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 0, 9)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expected, actual)
        
        
    def test_get_number_of_inversions_naive_example_1(self):
        """ Test get_number_of_inversions_naive with [2, 3, 9, 2, 9]."""
        inv = DivideAndConquer()
        actual = inv.get_number_of_inversions_naive([2, 3, 9, 2, 9])
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_number_of_inversions_naive_example_2(self):
        """ Test get_number_of_inversions_naive with [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]."""
        inv = DivideAndConquer()
        actual = inv.get_number_of_inversions_naive([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected = 45
        self.assertEqual(expected, actual)
        
        
    def test_get_number_of_inversions_fast_example_1(self):
        """ Test get_number_of_inversions_fast with [2, 3, 9, 2, 9]."""
        inv = DivideAndConquer()
        actual = inv.get_number_of_inversions_fast([2, 3, 9, 2, 9])
        expected = 2
        self.assertEqual(expected, actual)
        
        
    def test_get_number_of_inversions_fast_example_2(self):
        """ Test get_number_of_inversions_fast with [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]."""
        inv = DivideAndConquer()
        actual = inv.get_number_of_inversions_fast([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected = 45
        self.assertEqual(expected, actual)
        
        
    def test_merge_sort_example_1(self):
        """ Test merge_sort with [2, 3, 9, 2, 9]."""
        inv = DivideAndConquer()
        actual = inv.merge_sort([2, 3, 9, 2, 9])
        expected = [2, 2, 3, 9, 9]
        self.assertEqual(expected, actual)
        
        
    def test_merge_sort_example_2(self):
        """ Test merge_sort with [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]."""
        inv = DivideAndConquer()
        actual = inv.merge_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(expected, actual)
        
        
    def test_count_segments_naive_example_1(self):
        """ Test count_segments_naive with [0, 7] [5, 10] [1, 6, 11]."""
        count_segments = DivideAndConquer()
        actual = count_segments.count_segments_naive([0, 7], [5, 10], [1, 6, 11])
        expected = [1, 0, 0]
        self.assertEqual(expected, actual)
        
        
    def test_count_segments_naive_example_2(self):
        """ Test count_segments_naive with [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]."""
        count_segments = DivideAndConquer()
        actual = count_segments.count_segments_naive([0, -3, 7], [5, 2, 10], [1, 6])
        expected = [2, 0]
        self.assertEqual(expected, actual)
        
        
    def test_sort_and_count_segments_example_1(self):
        """ Test sort_and_count_segments with [0, 7] [5, 10] [1, 6, 11]."""
        count_segments = DivideAndConquer()
        actual = count_segments.sort_and_count_segments([0, 7], [5, 10], [1, 6, 11])
        expected = [1, 0, 0]
        self.assertEqual(expected, actual)
        
        
    def test_sort_and_count_segments_example_2(self):
        """ Test sort_and_count_segments with [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]."""
        count_segments = DivideAndConquer()
        actual = count_segments.sort_and_count_segments([0, -3, 7], [5, 2, 10], [1, 6])
        expected = [2, 0]
        self.assertEqual(expected, actual)
        
        
    def test_closest_points_naive_example_1(self):
        """ Test closest_points_naive with [7, 1, 4, 7], [7, 100, 8, 7]."""
        min_dist = DivideAndConquer()
        actual = min_dist.closest_points_naive([7, 1, 4, 7], [7, 100, 8, 7])
        expected = 0.0
        self.assertEqual(expected, actual)
        
        
    def test_closest_points_naive_example_2(self):
        """ Test closest_points_naive with [4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2],
                                           [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4]."""
        min_dist = DivideAndConquer()
        actual = min_dist.closest_points_naive([4, -2, -3, -1, 2, -4, 1, -1, 3, -4, -2],
                                               [4, -2, -4, 3, 3, 0, 1, -1, -1, 2, 4])
        expected = 1.4142135623730951
        self.assertEqual(expected, actual)
        
if __name__ == '__main__':
    unittest.main(exit=False)
    
