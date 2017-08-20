import cProfile
from intro_to_algorithmic_toolbox import IntroToAlgorithmicToolbox


def cprofile_intro_to_algorithmic_toolbox():
    number = IntroToAlgorithmicToolbox()
    profile = cProfile.run('number.get_nth_fib_number_recur(0)')
    
    number = IntroToAlgorithmicToolbox()
    profile = cProfile.run('number.get_nth_fib_number_recur(30)')
    
    number = IntroToAlgorithmicToolbox()
    profile = cProfile.run('number.get_nth_fib_number_iter(30)')
    
    number = IntroToAlgorithmicToolbox()
    profile = cProfile.run('number.get_nth_fib_number_iter(10**3)')
    
    number = IntroToAlgorithmicToolbox()
    profile = cProfile.run('number.get_fibonacci_last_digit_naive(31)')
    
    number = IntroToAlgorithmicToolbox()
    profile = cProfile.run('number.get_fibonacci_last_digit_naive(30)')


if __name__ == '__main__':
    print(cprofile_intro_to_algorithmic_toolbox())