#!/usr/bin/env python
"""
In this excercise we will learn the general usage of functions and flow control in a python script. 
We ask you to implemant a fucntion  to calculate the first n numbers of the Fibonacci series. 
The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. 
The first 6 numbers of the Fibonacci series would then be: 1,1,2,3,5,8
You should design a program that calculates the first n numbers of the Fibonacci series (having as the two starting numbers: 1,1)
and saves them in a list that at the end of the program will be printed.
"""



"""
Put your code in this section of the script:
"""



def generate_fibonacci(n):
    """ Counts the number of words (separated by white spaces or newlines) in a text """
    pass


# call function & print output
list_fibonacci = generate_fibonacci(n)





"""
From here on unit tests.
Do not modify this code!
"""

def test_list_fibonacci():
    list_fibonacci = generate_fibonacci(100)
    assert list_fibonacci[-1] == 927372692193078999176
    assert list_fibonacci[0] == 1
    assert list_fibonacci[1] == 1

    list_fibonacci = generate_fibonacci(0)
    assert list_fibonacci[-1] == 1
    assert len(list_fibonacci) == 2


if __name__ == '__main__':
    from test_runner import run_tests
    run_tests()