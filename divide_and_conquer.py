import math, random

class DivideAndConquer(object):
    """ Divide and conquer. """
    
    
    def __init__(self):
        pass
    
    
    def linear_search(self, num_lst, key):
        """(DivideAndConquer, list of numbers, number) -> integer
        
        Return the index of key if key exists in list num_lst. Otherwise, return -1.
        """
        # Running time: O(n)
        for i in range(len(num_lst)):
            if num_lst[i] == key:
                return i
            
        return -1
    
    
    def binary_search(self, num_lst, key):    
        """(DivideAndConquer, list of numbers, number) -> integer
        
        Return the index of key if key exists in list num_lst. Otherwise, return -1.
        
        Precondition: num_lst must be sorted in ascending order
                      1 <= num_lst_i <= 10 ** 9
        """
        # Running time: O(log n) with O(n logn) overhead
        # get sorted list
        num_lst = sorted(num_lst)
        
        low, high, idx = 0, len(num_lst), -1
        
        while low < high:
            mid = int(math.floor((low+high) / 2.0))
            
            if key < num_lst[mid]: high = mid - 1
            elif key > num_lst[mid]: low = mid + 1
            elif key == num_lst[mid]: 
                idx = mid
                return idx
            
        return idx
    
    
    def get_majority_element_naive(self, lst, left, right):
        """(DivideAndConquer, list of numbers, integer, integer) -> number
        
        Return the majority value if the majority value exists. Otherwise, return -1.
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        # Running time: O(n ** 2)
        n = len(lst)
        
        for i in range(n):
            current_elem, count = lst[i], 0
            for j in range(n):
                if lst[j] == current_elem:
                    count += 1
                    
            if count > int(math.floor(n / 2.0)): return lst[i]
            
        return -1
    
    
    def get_majority_element_sort_count(self, lst, left, right):
        """(DivideAndConquer, list of numbers, integer, integer) -> number
        
        Return the majority value if the majority value exists. Otherwise, return -1.
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        # get sorted list
        sorted_lst = sorted(lst)
        
        n = len(sorted_lst)
    
        for i in range(n):
            count = sorted_lst.count(sorted_lst[i])
            if count > int(math.floor(n / 2.0)): return sorted_lst[i]
            
        return -1
    
    
    def get_majority_element_linear(self, lst):
        """(DivideAndConquer, list of numbers, integer, integer) -> number
        
        Return the majority value if the majority value exists. Otherwise, return -1.
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        # Idea: Boyer–Moore majority vote algorithm (O(n) time)
        lst, n = sorted(lst), len(lst)
        
        if n <= 2:
            if lst[0] == lst[1]: return 1
            else: return -1
        
        temp_lst, count = [], 1
        for i in range(n-1):
            if lst[i] == lst[i+1]:
                temp_lst.append(lst[i])
                count += 1
            else: 
                if count > int(math.floor(n / 2.0)): return count
                else: count = 1
            i += 1
        
        return -1
    
    
    def partition_2_way(self, lst, left, right):
        """(DivideAndConquer, list of items, integer, integer) -> integer
        """
        pivot, j = lst[left], left
        
        for i in range(left + 1, right + 1):
            if lst[i] <= pivot:
                j += 1
                lst[i], lst[j] = lst[j], lst[i]
                
        lst[left], lst[j] = lst[j], lst[left]
        
        return j


    def randomized_quick_sort_2_way_p(self, lst, left, right):
        """(DivideAndConquer, list of items, integer, integer) -> list of items
        
        Return the sorted (nod-decreasing order) list.
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        if left >= right:
            return
        
        k = random.randint(left, right)
        lst[left], lst[k] = lst[k], lst[left]
    
        m = self.partition_2_way(lst, left, right)
        
        self.randomized_quick_sort_2_way_p(lst, left, m - 1);
        self.randomized_quick_sort_2_way_p(lst, m + 1, right);
        
        return lst
    
    
    def partition_3_way(self, lst, left, right):
        """(DivideAndConquer, list of items, integer, integer) -> integer
        
        Return the lower and upper indices of duplicate keys. 
        """
        # Idea: item less than pivot, move to the left; item greater than 
        # pivot, move to the right.
        pivot, j, k, i = lst[left], left, right, left
    
        while i <= k:
            if lst[i] < pivot: 
                lst[j], lst[i] = lst[i], lst[j]
                j += 1
                i += 1
            elif lst[i] > pivot:
                lst[k], lst[i] = lst[i], lst[k]
                k -= 1
            else: i += 1
            
        return j, k


    def randomized_quick_sort_3_way_p(self, lst, left, right):
        """(DivideAndConquer, list of items, integer, integer) -> list of items
        
        Return the sorted (nod-decreasing order) list.
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        if left >= right:
            return
        
        k = random.randint(left, right)
        lst[left], lst[k] = lst[k], lst[left]
        
        m1, m2 = self.partition_3_way(lst, left, right)
        
        self.randomized_quick_sort_3_way_p(lst, left, m1 - 1);
        self.randomized_quick_sort_3_way_p(lst, m2 + 1, right);
        
        return lst
    
    
    def get_number_of_inversions_naive(self, lst):
        """(DivideAndConquer, list of items) -> integer
        
        Return the number of inversion in the input list.
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        # Running time: O(n ** 2)
        count_inv = 0
        
        for i in range(len(lst)):
            for j in range(i+1, len(lst)):
                if lst[i] > lst[j]:
                    count_inv += 1
                    
        return count_inv
    
    
    def sort_and_get_number_of_inversions(self, lst):
        """(DivideAndConquer, list of items) -> list of items, integer
        
        Return sorted (non-decreasing order) list and number of inversion in the unsorted list.
        """
        n = len(lst)
        if n == 1: return lst, 0 
        
        mid = int(n / 2)
        first_half_lst = lst[0:mid]
        second_half_lst = lst[mid:n]
        
        sorted_lst_a, inv_a = self.sort_and_get_number_of_inversions(first_half_lst)
        sorted_lst_b, inv_b = self.sort_and_get_number_of_inversions(second_half_lst)
            
        sorted_lst, cross_inv = self.merge_and_get_number_of_inversions(sorted_lst_a, sorted_lst_b)
        
        return sorted_lst, (inv_a + inv_b + cross_inv)  


    def merge_and_get_number_of_inversions(self, sorted_lst_a, sorted_lst_b):
        """(DivideAndConquer, list of items, list of items) -> list of items, integer
        
        Return a merged list of items from the two given sorted lists, and
        the number of cross inversions.
        """
        a, b, cross_inv_count, out_lst = 0, 0, 0, []
        
        while a < len(sorted_lst_a) and b < len(sorted_lst_b):
            next_ = min(sorted_lst_a[a], sorted_lst_b[b])
            out_lst.append(next_)
                    
            if sorted_lst_a[a] > sorted_lst_b[b]: 
                b += 1
                cross_inv_count += len(sorted_lst_a) - a # get cross inversion
            else: a += 1
                
        # append the rest of sorted_lst_a and sorted_lst_b to d_lst       
        [out_lst.append(sorted_lst_a[a]) for a in range(a, len(sorted_lst_a))]
        [out_lst.append(sorted_lst_b[b]) for b in range(b, len(sorted_lst_b))]
            
        return out_lst, cross_inv_count 
    
    
    def merge_sort(self, lst):
        """(list of items) -> list of items
        
        Return the sorted (nod-decreasing order) list. 
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        [sorted_lst, number_of_inversions] = self.sort_and_get_number_of_inversions(lst)
        
        return sorted_lst
    

    def get_number_of_inversions_fast(self, lst):
        """(list of items) -> integer
        
        Return the total number of inversions in the list.
        
        Precondition: 1 <= length(lst) <= 10 ** 5
                      0 <= lst_i <= 10 ** 9 for all 0 <= i < length(lst)
        """
        [sorted_lst, number_of_inversions] = self.sort_and_get_number_of_inversions(lst)
        
        return number_of_inversions
    
    
    def count_segments_naive(self, starts, ends, points):
        """(DivideAndConquer, list of numbers, list of numbers) -> list of numbers
        
        Return the number of segments ([starts, ends]) that contains the given points.
        
        Precondition: 1 <= length(starts) <= 5 * (10 ** 5)
                      1 <= length(ends) <= 5 * (10 ** 5)
                      1 <= length(points) <= 5 * (10 ** 5)
                      (-1) * (10 ** 8) <= starts_i <= ends_i <= 10 ** 8 for all 1 <= i < segments([starts, ends])
         """
        count = [0] * len(points)
        
        for i in range(len(points)):
            for j in range(len(starts)):
                if starts[j] <= points[i] <= ends[j]:
                    count[i] += 1
                    
        return count
    
    
    def binary_search_for_count_segments(self, sorted_lst, key):   
        """(DivideAndConquer, list of numbers, number) -> number
        
        Return key if key exists in list num_lst.
        
        Precondition: num_lst must be sorted in ascending order
                      1 <= num_lst_i <= 10 ** 9
        """
        low, high, val = 0, len(sorted_lst) - 1, -1
        
        while low <= high:
            mid = int(math.floor((low+high) / 2.0))
            
            if key < sorted_lst[mid]:
                high = mid - 1
            elif key > sorted_lst[mid]:
                low = mid + 1
            elif key == sorted_lst[mid]:
                idx = mid
                val = sorted_lst[idx]
                return val
            else: 
                return val
            
        return val
    
    
    def sort_and_count_segments(self, starts, ends, points):
        """(DivideAndConquer, list of numbers, list of numbers) -> list of numbers
        
        Return the number of segments ([starts, ends]) that contains the given points.
        
        Precondition: 1 <= length(starts) <= 5 * (10 ** 5)
                      1 <= length(ends) <= 5 * (10 ** 5)
                      1 <= length(points) <= 5 * (10 ** 5)
                      (-1) * (10 ** 8) <= starts_i <= ends_i <= 10 ** 8 for all 1 <= i < segments([starts, ends])
         """
        
        # Cons: needs lot of memeory space
        lst = []
        for i in range(len(starts)):    
            lst.append(range(starts[i], ends[i]+1))
        
        # store all the items in list
        lst_2 = []
        for sublist in lst:
            for item in sublist:
                lst_2.append(item)
        
        sorted_lst_2 = sorted(lst_2) # get sorted list
        
        count = [0] * len(points)
        
        # find item via binary search and count the occuranace of the item.
        for i in range(len(points)):
            if self.binary_search_for_count_segments(sorted_lst_2, points[i]) == points[i]:
                count[i] += sorted_lst_2.count(points[i])
                
        return count
    
    
    def get_euclidean_distance(self, x_coord_1, x_coord_2, y_coord_1, y_coord_2):
        """(DivideAndConquer, number, number, number, number) -> number
        
        Return euclidean distance between a pair of two different points.
        """

        return math.sqrt(((x_coord_1 - x_coord_2) ** 2) + \
                         ((y_coord_1 - y_coord_2) ** 2))


    def closest_points_naive(self, x, y):
        """(DivideAndConquer, list of numbers, list of numbers) -> number
        
        Return the smallest distance between a pair of two different points.
        
        Precondition: 1 <= length(x) <= 10 ** 5
                      (-1) * (10 ** 9) <= x_i <= 10 ** 9
                      (-1) * (10 ** 9) <= y_i <= 10 ** 9
        """
        # Running time: O(n ** 2)

        dist = []
        for i in range(len(x)):
            for j in range(i+1, len(x)):
                d = self.get_euclidean_distance(x[i], x[j], y[i], y[j])
                dist.append(d)
    
        return min(dist)

    

