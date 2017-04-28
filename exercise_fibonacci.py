#!/usr/bin/env python
"""
In this excercise we will learn the general usage of functions and flow control
in a python script. We ask you to implement a function to calculate the first
n numbers of the Fibonacci series.
The Fibonacci series is a series of numbers in which each number is the sum of
the two preceding numbers, given that the first two Fibonacci numbers are both
1. The first 6 numbers of the Fibonacci series are therefore: 1,1,2,3,5,8
You should design a program that calculates the first n numbers of the
Fibonacci series (having as the two starting numbers: 1,1) and saves them in
a list that at the end of the program will be printed.
"""


"""
Put your code in this section of the script:
"""


def generate_fibonacci(n):
    """Returns a list of the first n Fibonacci numbers"""
    pass


"""
From here on unit tests.
Do not modify this code!
"""


def test_empty_fibonacci_list():
    list_fibonacci = generate_fibonacci(0)
    assert len(list_fibonacci) == 0


def test_long_fibonacci_list():
    list_fibonacci = generate_fibonacci(100)
    assert list_fibonacci[-1] == 927372692193078999176
    assert list_fibonacci[0] == 1
    assert list_fibonacci[1] == 1


if __name__ == '__main__':
    from test_runner import run_tests
    print('The first ten Fibonacci numbers are {}'.format(generate_fibonacci(10)))
    run_tests()
