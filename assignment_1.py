solution_student = []

# Assignment 01:
# x = [1,2]
# y = [1,2]
# x == y ?? True or False ?

# Assignment 02:
# x = [1,2]
# y = [1,2]
# x is y ?? True or False ?

# Assignment 03:
# x = [1,2]
# y = x
# x == y ?? True or False ?

# Assignment 04:
# x = [1,2]
# y = x
# x is y ?? True or False ?

if __name__ == '__main__':
    import _pickle
    with open('./solution/solution_1.pkl', 'rb') as solution_file:
        solution_tutors = _pickle.load(solution_file)
    if solution_tutors == solution_student:
        print('Solved!')
    else:
        print('Try Again!')
