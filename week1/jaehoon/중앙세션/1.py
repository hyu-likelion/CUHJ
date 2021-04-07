from bwsi_grader.python.palindrome import grader

def student_func(x):
    x = x.lower().replace(" ","")
    L = len(x)
    for i in range(L):
        if x[i] != x[-i-1]:
            return False

    return True