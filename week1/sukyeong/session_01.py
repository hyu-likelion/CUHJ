x = "Race car"


def student_func(x):
    answer = True
    x = list(x.lower())
    x = ' '.join(x).split()
    count = -1
    for i in range(int(len(x) / 2)):
        if x[i] != x[count]:
            answer = False
        else:
            count = count - 1
    return answer

print(student_func(x))
