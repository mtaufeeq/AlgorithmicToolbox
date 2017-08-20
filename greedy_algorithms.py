class GreedyAlgorithms(object):
    """ Greedy Algorithms."""
    
    
    def __init__(self):
        pass
    
    
    def get_change(self, money):
        """(GreedyAlgorithms, integer) -> integer
        
        Return minimum number of coins with denominations 1, 5, and 10 that changes money.
        
        Precondition: 1 <= money <= 10 ** 3
        """
        n_coin_10 = money // 10
        r_coin_10 = money % 10
        
        n_coin_5 = r_coin_10 // 5
        r_coin_5 = r_coin_10 % 5
        
        n_coin_1 = r_coin_5 // 1
        r_coin_1 = r_coin_5 % 1
        
        min_coins = sum([n_coin_10, n_coin_5, n_coin_1])
        
        return min_coins
    
    
    def get_sorted_values_weights(self, weights, values):
        """(GreedyAlgorithms, list of numbers, list of numbers) -> list of numbers, list of numbers, 
        list of numbers
        
        Return sorted (non-increasing order) values over weights, values and weights. 
        """    
        v_w = []
        for i in range(len(weights)):
            v_w.append(float(values[i]) / weights[i])
    
        # Zip them up and sort in descending order
        zs_v_w_values_weights = sorted(zip(v_w, values, weights), \
                                       reverse = True)
        
        # extract lists
        v_w = [x[0] for x in zs_v_w_values_weights]
        values = [x[1] for x in zs_v_w_values_weights]
        weights = [x[2] for x in zs_v_w_values_weights]
        
        return v_w, values, weights


    def get_optimal_value_of_fractional_knapsack(self, capacity, weights, values):
        """(GreedyAlgorithms, number, list of numbers, list of numbers) -> float
        
        Return the optimal value of the fractional Knapsack.
        
        Precondition: 0 <= capacity <= 2 * (10 ** 6)
                      0 <= weights_i, values_i <= 2 * (10 ** 6) for 1 <= i <= n
        """
        # Idea: greedy approach
        value = 0. # optimal value in knapsack
        amount_list = [0] * len(weights)**2
    
        # get ordered lists
        v_w, values, weights = self.get_sorted_values_weights(weights, values)
        
        for i in range(len(weights)):
            if capacity == 0: return value
            
            a = min(weights[i], capacity)
            value = value + (a * v_w[i])
            weights[i] -= a
            amount_list.append(a)
            capacity -= a
            
        return round(value, 4)
    
    
    def get_sorted_profit_click(self, profits, clicks):
        """(GreedyAlgorithms, list of numbers, list of numbers) -> list of numbers, list of numbers
        
        Return sorted (descending order) list of profits and clicks.
        """ 
        profits = sorted(profits, reverse = True)
        clicks = sorted(clicks, reverse = True)
        
        return profits, clicks


    def get_max_sum_of_dot_product(self, lst_a, lst_b):
        """(GreedyAlgorithms, list of numbers, list of numbers) -> number
        
        Return maximized sum of the dot product of values in sorted lists lst_a and lst_b.
        
        Precondition: (-1) * (10 ** 5) <= lst_a_i, lst_b_i <= 10 ** 5 for all 1 <= i <= n
        """
        # Idea: greedy approach. multiply probable large number with probable large number
        # get sorted lists
        lst_a, lst_b = self.get_sorted_profit_click(lst_a, lst_b)
        
        res = 0
        for i in range(len(lst_a)):
            res += lst_a[i] * lst_b[i]
            
        return res
    
    
    def get_optimal_summands(self, n):
        """(GreedyAlgorithms, integer) -> list of integers
        
        Return list of pairwise of distinct positive integers that sum up to n.
        
        Precondition: 1 <= n <= 10 ** 9
        """
        # Idea: greedy approach
        summands = []
        l, k = 1, n
        sum_ = sum(summands)
        
        while sum_ <= n:
            if k <= (2*l):
                summands.append(k)
                return summands
            
            summands.append(l)
            k -= l
            l += 1
                
        return summands
    
    
    def partition_2_way_for_salary_max(self, lst, left, right):
        """(GreedyAlgorithms, list of numbers, integer, integer) -> integer
        """
        # Idea: modified quick sort partitioning
        # Partition: 1. convert number to string
        #            2. add strings
        #            3. convert strings back to s_numbers
        #            4. compare s_numbers
        #            5. exchange numbers
        pivot, j = lst[left], left
        
        for i in range(left + 1, right + 1):
            lst_i, pivot_i = str(lst[i]), str(pivot)

            s1 = int(lst_i + pivot_i)
            s2 = int(pivot_i + lst_i)
            
            if s1 >= s2:
                j += 1
                lst[i], lst[j] = lst[j], lst[i]
                
        lst[left], lst[j] = lst[j], lst[left]
        
        return j


    def quick_sort_for_salary_max(self, lst, left, right):
        """(GreedyAlgorithms, list of numbers, integer, integer) -> list of numbers
        
        Return sorted list (descending order) 
        """
        if left >= right:
            return
        
        m = self.partition_2_way_for_salary_max(lst, left, right)
        
        self.quick_sort_for_salary_max(lst, left, m - 1);
        self.quick_sort_for_salary_max(lst, m + 1, right);
        
        return lst


    def get_largest_number(self, digits):
        """(GreedyAlgorithms, list of numbers) -> number
        
        Return the largerst number that can be composed out of list of digits.
        
        Precondition: 1 <= digits <= 100
                      1 <= digit_i <= 10 ** 3 for all 1 <= i <= n
        """
        left, right = 0, len(digits) - 1

        ordered_lst = self.quick_sort_for_salary_max(digits, left, right) # get sorted list
        
        # Append numbers to string to maximzie salary
        res = ''
        for number in range(len(ordered_lst)):
            res += str(ordered_lst[number])
            
        return res
 