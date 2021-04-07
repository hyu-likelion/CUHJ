from bwsi_grader.python.three_five import grader
#threefive
def student_func(num : int) -> str :
    answer = num
    if num % 15 == 0 :
        answer = 'threefive'
        return answer
    elif num % 3 == 0 :
        answer = "three"
        return answer
    elif num % 5 == 0 :
        answer = "five"
        return answer
    else :
        return answer
    pass

grader(student_func)
