# import sys
# input = sys.stdin.readline

def student_func(x):
    x = int(x)

    if x%3 == 0 :
        if x%5 == 0 :
            return "threefive"
        else :
            return "three"

    elif x%5 == 0 :
        if x%3 == 0 :
            return "threefive" 

        else :
            return "five"

    else :
        return x



# print(student_func(3))
# print(student_func(5))
# print(student_func(15))
# print(student_func(2))


# Execute this cell to grade your work
from bwsi_grader.python.three_five import grader
grader(student_func)
grader(student_func)