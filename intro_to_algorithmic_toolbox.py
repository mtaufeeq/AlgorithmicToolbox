# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:00:03 2017

@author: Md. Taufeeq Uddin
"""
class IntroToAlgorithmicToolbox(object):
    """ Naive to fast implementation of classic algorithmic problems."""
    
    def __init__(self):
        pass
    
    
    def get_nth_fib_number_recur(self, number):
        """(IntroToAlgorithmicToolbox, number) -> number
        
        Return nth Fibonacci number for a given number n.
        
        Precondition: 0 <= number <= 45
        """
        if number <= 1: return number

        return self.get_nth_fib_number_recur(number - 1) +\
    self.get_nth_fib_number_recur(number - 2)

    
    def get_nth_fib_number_iter(self, number):
        """(IntroToAlgorithmicToolbox, number) -> number
        
        Return nth Fibonacci number for a given number.
        
        Precondition: 0 <= number <= 10 ** 7
        """
        if number <= 1: return number
        else:
            number += 1
    
            fib_list = []  # create a list of fibonacci numbers
            [fib_list.append(i) for i in range(number)]
                
            fib_list[0], fib_list[1] = 0, 1
            for i in range(2, number):
                fib_list[i] = fib_list[i - 1] + fib_list[i - 2] 
    
            return fib_list[len(fib_list) - 1] # return nth Fibonacci number
        
        
    def get_last_digit_of_fib_naive(self, number):
        """(IntroToAlgorithmicToolbox, number) -> number
        
        Return the last digit of the nth number of Fibonacci series.
        
        Precondition: 0 <= number <= 10 ** 5
        """
        if number <= 1: return number
    
        previous, current = 0, 1    
        for _ in range(number - 1):
            previous, current = current, previous + current
    
        return current % 10
    
    
    def get_last_digit_of_fib_str(self, number):
        """"(IntroToAlgorithmicToolbox, number) -> number
        
        Return the last digit of the nth number of Fibonacci series.
        
        Precondition: 0 <= number <- 10 ** 7
        """
        # Idea: get the nth number of Fibonacci series
        # convert the number to string
        nth_number = str(self.get_nth_fib_number_iter(number))
        
        return int(nth_number[len(nth_number)-1]) # return last character as integer
        

    def get_last_digit_of_fib_fast(self, number):
        """(IntroToAlgorithmicToolbox, number) -> number
        
        Return the last digit of the nth number of Fibonacci series.
        
        Precondition: 0 <= number <- 10 ** 7
        """
        # Idea: just store the last digit of number instead of the whole number
        if number <= 1: return number
        else:
            number += 1
    
            # create a list of Fibonacci numbers
            fib_list = []
            [fib_list.append(i) for i in range(number)]
                
            fib_list[0], fib_list[1] = 0, 1
            
            # for the ith value, compute Fibonacci modulous 10
            for i in range(2, number):
                fib_list[i] = (fib_list[i-1] + fib_list[i-2]) % 10
    
            # return last digit of nth Fibonacci number
            return fib_list[len(fib_list)-1]
        
        
    def gcd_naive(self, integer_a, integer_b):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return the greatest common divisor (GCD) of parameter a and b.
        """
        current_gcd = 1
        for d in range(2, min(integer_a, integer_b) + 1):
            if integer_a % d == 0 and integer_b % d == 0:
                if d > current_gcd:
                    current_gcd = d
                    
        return current_gcd
    
    
    def euclid_gcd(self, integer_a, integer_b):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return the greatest common divisor (GCD) of the given input 
        integer_a and integer_b.
        
        Precondition: 1 <= integer_a, integer_b <= 2 * (10 ** 9)
        """
        # Idea: Euclidean approach
        if integer_b == 0: return integer_a
        else: integer_a_prime = integer_a % integer_b
            
        return self.euclid_gcd(integer_b, integer_a_prime)
    
    
    def lcm_naive(self, integer_a, integer_b):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return the least common multiple (LCM) of given input integer_a and integer_b.
        """
        for l in range(1, integer_a * integer_b + 1):
            if l % integer_a == 0 and l % integer_b == 0:
                return l
    
        return integer_a * integer_b
    
    
    def lcm_euclid_gcd(self, integer_a, integer_b):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return the least common multiple (LCM) of given input integer_a and integer_b.
        
        Precondition: 1 <= integer_a, integer_b <= 2 * (10 ** 9)
        """    
        # Idea: LCM(integer_a, integer_b) * GCD(integer_a, integer_b) = integer_a * integer_B
        # call euclid_gcd to compute GCD and perform integer division 
        # before multiplication.
        return int((integer_a // self.euclid_gcd(integer_a, integer_b)) * integer_b)


    def get_fibonacci_huge_mod_m_naive(self, n, m):
        """ (IntroToAlgorithmicToolbox, number, number) -> number
        
        Return the remainder of Fibonacci number n when divided by m.
        """
        if n <= 1: return n
    
        previous, current = 0, 1
        for _ in range(n - 1):
            previous, current = current, previous + current
    
        return current % m
    
    
    def get_pisano_period(self, m):
        """(IntroToAlgorithmicToolbox, integer) -> integer
        
        Return the Pisano period for the given integer m.
        """
        int_a, int_b = 0, 1
        int_c = int_a + int_b
    
        x = 0
        while x < m*m:
            x += 1
            int_c = (int_a + int_b) % m
            int_a = int_b
            int_b = int_c
            
            if int_a==0: # Pisano period starts with 01
                if int_b==1:
                    return x
                
    
    def get_fibonacci_remainder(self, n, m):
        """(IntroToAlgorithmicToolbox, integer, integer) -> number
        
        Return remainder of Fibonacci number n feeding Pisano period of m.
        """
        # get Pisano period before performing mod operation
        return n % (self.get_pisano_period(m)) 
    
    
    def get_fibonacci_huge_mod_m_fast(self, n, m):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return the result of huge Fibonacci number n modulus m.
        
        Precondition: 1 <= n <= 10 ** 18, 2 <= m <= 10 ** 5
        """
        n = self.get_fibonacci_remainder(n, m) + 1 # get remainder
        
        if n <= 1: return 0
        else:    
            fib_list = []
            [fib_list.append(i) for i in range(n)]
                
            fib_list[0], fib_list[1] = 0, 1
            for i in range(2, n):
                fib_list[i] = (fib_list[i-1] + fib_list[i-2]) % m # just store the remainder
    
            return fib_list[len(fib_list)-1]
        
        
    def get_mod_of_sum_of_last_fib_digits_naive(self, n):
        """(IntroToAlgorithmicToolbox, integer) -> integer
        
        Return last digit of the sum of first n Fibonacci numbers.
        """
        if n <= 1: return n
    
        previous, current, sum = 0, 1, 1
        for _ in range(n - 1):
            previous, current = current, previous + current
            sum += current
    
        return sum % 10
    
    
    def get_list_of_remainder_of_fibonacci_numbers(self, n, m):
        """(IntroToAlgorithmicToolbox, integer, integer) -> list of integer
        
        Return list of remainders of n Fibonacci numbers.
        
        Precondition: 0 <= n <= 10 ** 14, m = 10
        """
        n = self.get_fibonacci_remainder(n, m) + 1 # get remainder
    
        if n <= 1: return 0
        else:
            fib_list = []
            [fib_list.append(i) for i in range(n)]
    
            fib_list[0], fib_list[1] = 0, 1
            for i in range(2, n):
                fib_list[i] = (fib_list[i-1] + fib_list[i-2]) % m
                
            return fib_list
        
        
    def get_last_digit_of_sum_of_fibonacci_numbers(self, n):
        """(IntroToAlgorithmicToolbox, integer) -> integer
        
        Return last digit of the sum of n Fibonacci numbers.
        """
        n = self.get_list_of_remainder_of_fibonacci_numbers(n, 10) # get Fibonacci list mod m
        
        if n == 0: return 0
        else: return sum(n) % 10
        
        
    def fibonacci_mod_of_partial_sum_naive(self, from_, to):
        """IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return last digit of the paritial sum of n Fibonacci numbers.
        """
        sum, current, next = 0, 0, 1
    
        for i in range(to + 1):
            if i >= from_:
                sum += current
    
            current, next = next, current + next
    
        return sum % 10
        
        
    def get_mod_of_sum_of_last_digits_partial(self, from_, to):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return last digit of the paritial sum of n Fibonacci numbers.
        
        Precondition: 0 <= from_ <= to <= 10 ** 18
        """
        # Flawed - failed in some cases
        n = self.get_list_of_remainder_of_fibonacci_numbers(to, 10) # get Fibonacci list mod m

        if n == 0: return 0
        else: return sum(n[from_: to + 1]) % 10
        
        
    def get_sum_of_n_fibonacci_numbers(self, n, m):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return the sum of the n Fibonacci numbers.
        """
        # Flaw: Need too much memory
        if n <= 1: return 0
        else:
            fib_list = []
            [fib_list.append(i) for i in range(n + 3)]
    
            fib_list[0], fib_list[1] = 0, 1        
            for i in range(2, n + 3):
                fib_list[i] = (fib_list[i-1] + fib_list[i-2]) 
                
            return fib_list[-1] - 1
        
        
    def get_partial_sum_of_fibonacci_series(self, from_, to):
        """(IntroToAlgorithmicToolbox, integer, integer) -> integer
        
        Return the sum of the n Fibonacci numbers.
        """
        # get sum of Fibonacci numbers
        from_val = self.get_sum_of_n_fibonacci_numbers(from_ - 1, 10)
        to_val = self.get_sum_of_n_fibonacci_numbers(to, 10)
        
        return abs(from_val - to_val) % 10 # return last digit
