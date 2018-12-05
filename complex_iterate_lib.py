"""
Problem Set 8 Complex Number Iterations
NAME : Nikita Lebedz

"""
import os


def do_calculation(complex_num, complex_seed):

    squared_complex = complex_num * complex_num

    squared_complex_plus_seed = squared_complex + complex_seed

    return squared_complex_plus_seed



def do_iteration(complex_num, complex_seed):

    new_complex_num = do_calculation(complex_num, complex_seed)

    for i in range(256):

        if abs(new_complex_num) > 2:
            break
        else:
            new_complex_num = do_calculation(new_complex_num, complex_seed)

    return(i)
