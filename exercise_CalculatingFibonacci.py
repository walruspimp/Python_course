from test_runner import run_tests


# Task 1
# The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. 
# The first 6 numbers of the Fibonacci series would then be: 1,1,2,3,5,8
# You should design a program that calculates the first 1000 numbers of the Fibonacci series (having as the two starting numbers: 1,1)
# and saves them in a list that at the end of the program will be printed.


# ________________________________________
# Your code here



# define function
def generate_fibonacci(nend)


# call function (with user input)
list_fibonacci = generate_fibonacci(nend)
print(list_fibonacci)
    


# ________________________________________
# test part, do not change
def test_list_fibonacci():
   list_fibonacci = generate_fibonacci(100)
   assert list_fibonacci[-1] == 927372692193078999176
   assert list_fibonacci[0] == 1
   assert list_fibonacci[1] == 1

   list_fibonacci = generate_fibonacci(0)
   assert list_fibonacci[-1] == 1
   assert len(list_fibonacci) == 2


if __name__ == '__main__':
   run_tests()



