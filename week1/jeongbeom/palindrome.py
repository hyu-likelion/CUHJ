from bwsi_grader.python.palindrome import grader
#palindrome
def student_func(word : str) -> bool :
    answer = False
    word = word.lower()
    word = ''.join(word.split())
    word_reverse = word[::-1]
    if word == word_reverse :
        answer = True
        return answer
    return answer
    pass
grader(student_func)
