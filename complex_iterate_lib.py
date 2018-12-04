"""
Problem Set 8 Complex Number Iterations
NAME : Nikita Lebedz

complete the code for the functions below


"""
import os


def do_calculation(complex_num, complex_seed):
    """
    Takes two inputs, complex_num which is a complex number and
    a seed which is also a complex numberself.
    The calculation will square the complex number and then
    add the seed to it.

    Then return the new complex number
    """
    squared_complex = complex_num
    """* complex_num"""
    squared_complex_plus_seed = squared_complex + complex_seed
    return squared_complex_plus_seed








def do_iteration(complex_num, complex_seed):
    """
    Takes two inputs, a complex number and a seed which is also
    a complex numberself.
    You have made the do_calculation function above.  Use that here.
    We will do a calculation on the complex number and seed.
    Then take the resulting complex number as the new complex number and
    then do the calculation again with that new complex number and the same
    original seed.
    Keep doing this until EITHER
    (a) the new complex number get more than 2 "units" away from the origin
    OR
    (b) you have iterated 255 times

    When this has completed, return the number of iterations that executed
    """



    new_complex_num = do_calculation(complex_num, complex_seed)


    for i in range(255):
        list = []

        if abs(new_complex_num) <= 2:
            list.append(new_complex_num)
            how_many = len(list)
            return('amount of iteratins: {0}'.format(how_many))
        else:
            if (abs(new_complex_num)>2 and i<255):
                list.append(new_complex_num)
                new_complex_num = do_calculation(new_complex_num, complex_seed)
            else:
                return('iterated 255 times')


some_complex_num = 3
some_complex_seed = -0.1
print(abs(do_calculation(some_complex_num, some_complex_seed)))
print(do_iteration(some_complex_num, some_complex_seed))
