class DynamicProgramming(object):
    """ Dynamic programming. """
    
    def __init__(self):
        pass
    
    def get_optimal_weight_knapsack_with_no_rep(self, W, weights):
        """(DynamicProgramming, number, list of numbers) -> number
        
        Reutrn the maximum weight the fits into a knapsack (with no repetition) of capacity W.
        
        Preconditions: 1 <= W <= 10 ** 4
                       1 <= n = length(weights) <= 300
                       0 <= weights_i ... weights_n-1 <= 10 ** 5
        """
        n = len(weights)
        value = [[0] * (W + 1) for _ in range(n + 1)] 
        weights.insert(0, 0)
        
        for i in range(1, n + 1):
            for w in range(0, W + 1):
                if weights[i] <= w:
                    value[i][w] = max(value[i - 1][w], weights[i] + \
                         value[i - 1][w - weights[i]])
                else:
                    value[i][w] = value[i - 1][w]
                    
        return value[n][W]
    
    
    def get_edit_distance(self, s, t):
        """(DynamicProgramming, sring, string) -> integer
        
        Return the edit distnace between the given two strings s and t.
        
        Preconditions: 1 <= length(s), length(t) <= 100
        """
        n, m = len(s), len(t)
        
        # create and populate table
        dist_tab = [[0] * (m + 1) for _ in range(n + 1)]    
        dist_tab[0] = list(range(0, m + 1))
        for i in range(0, n + 1): dist_tab[i][0] = i
            
        for j in range(1, m + 1):
            for i in range(1, n + 1):
                insertion = dist_tab[i] [j - 1] + 1
                deletion = dist_tab[i - 1] [j] + 1
                match = dist_tab[i - 1] [j - 1]
                mismatch = dist_tab[i - 1] [j - 1] + 1
                
                if s[i - 1] == t[j - 1]:
                    dist_tab[i][j] = min(insertion, deletion, match)
                else:
                    dist_tab[i][j] = min(insertion, deletion, mismatch)
                    
        return dist_tab[n][m]
    
    
    def get_dp_tab(self, numbers_lst):
        """(DynamicProgramming, list of numbers) -> list of list of numbers
        
        Return list of list of numbers where right diagonal contains the value of numbers_lst
        and non right diagonal contains 0.
        """
    
        mat = [[0 for i in range(len(numbers_lst))] for j in range(len(numbers_lst))]
    
        for row in range(len(numbers_lst)):
            for col in range(len(numbers_lst)):
                if row == col:
                    mat[row][col] = numbers_lst[row]
                
        return mat


    def evaltor(self, a, b, op):
        """(DynamicProgramming, number, number, string) - > number
        
        Return the result of the performed arithmatic operation.
        """
        if op == '+': return a + b
        elif op == '-': return a - b
        elif op == '*': return a * b
        else: assert False
        
    
    def min_max(self, m, M, i, j, op):
        """(DynamicProgramming, list of list of numbers, list of list of numbers, integer, integer, list of symbols) -> number, number
        
        Return the minimum and maximum of the of performed arithmatic operations.
        """
        min_ = 10 ** 30
        max_ = (-1) * min_
        
        for k in range(i, j):
            a = self.evaltor(M[i - 1][k - 1], M[k][j - 1], op[k - 1])
            b = self.evaltor(M[i - 1][k - 1], m[k][j - 1], op[k - 1])
            c = self.evaltor(m[i - 1][k - 1], M[k][j - 1], op[k - 1])
            d = self.evaltor(m[i - 1][k - 1], m[k][j - 1], op[k - 1])
            
            min_ = min(min_, a, b, c, d)
            max_ = max(max_, a, b, c, d)
            
        return min_, max_

    
    def get_max_val_of_arith_expr_via_parentheses(self, expr):    
        """(DynamicProgramming, string) -> number
        
        Return the maximum value of the input arithmetic expression among
        different order of applying arithmetic operations.
        
        Precondition: length(expr) <= 29
        """
        numbers_lst, ops_lst = [], []
        
        # extract variables and operators
        for i in range(len(expr)):
            if i % 2 == 0: numbers_lst.append(int(expr[i]))
            else: ops_lst.append(expr[i])
               
        # create 2-d table    
        m = self.get_dp_tab(numbers_lst) 
        M = self.get_dp_tab(numbers_lst)
         
        n = len(numbers_lst)
    
        for s in range(1, n + 1):
            for i in range(1, (n - s) + 1):
                j = i + s
                m[i - 1][j - 1], M[i - 1][j - 1] = self.min_max(m, M, i, j, ops_lst)
                
        return M[0][n - 1]
    
    
    def get_longest_common_subsequence_3(self, lst1, lst2, lst3):
        """(DynamicProgramming, list of numbers, list of numbers, list of numbers) -> number
        
        Return the length of the longest common subsequence of three sequences. 
        
        Preconditions: (-1) * (10 ** 9) <= lst1_i, lst1_i, lst3_i <= 10 ** 9
                       1 <= m = length(lst1), n = length(lst2), p = length(lst3) <= 100
        """
        m, n, p = len(lst1), len(lst2), len(lst3)
        
        # create 2-d table
        subs_tab = [[[0 for k in range(p+1)] for j in range(n+1)] \
                      for i in range(m+1)]
        
        for i in range(len(lst1)):
            for j in range(len(lst2)):
                for k in range(len(lst3)):
                    if lst1[i] == lst2[j] and lst2[j] == lst3[k]:
                        subs_tab[i + 1][j + 1][k + 1] = subs_tab[i][j][k] + 1
                    else:
                        subs_tab[i + 1][j + 1][k + 1] = max(subs_tab[i + 1][j + 1][k],
                                subs_tab[i][j + 1][k + 1], subs_tab[i + 1][j][k + 1])
                        
        return subs_tab[m][n][p]

                