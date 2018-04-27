solution_student = []

# Assigment 1:
# x = [1,2]
# y = [1,2]
# x == y ?? True or False ?

# Assigment 2:
# x = [1,2]
# y = [1,2]
# x is y ?? True or False ?

# Assigment 3:
# x = [1,2]
# y = x
# x == y ?? True or False ?

# Assigment 4:
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
