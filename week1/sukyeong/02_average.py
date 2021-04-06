C = int(input())  # 테스트 케이스의 개수
test_list = [0]*C  # 테스트 케이스의 외부 리스트
test_average = []  # 각 테이트 케이스의 평균을 담을 리스트, 전역

# 테스트 케이스의 내부 리스트 입력 받기
for i in range(C):
    inner_list = list(map(int, input().split()))
    test_list[i] = inner_list


# 각 테이스 케이스의 평균을 구하는 함수
def average():
    global test_average
    for i in range(0, C):
        student_num = test_list[i][0]
        test_sum = 0
        for j in range(1, student_num+1):
            test_sum = test_sum + test_list[i][j]
        test_average.append(test_sum / student_num)

    return test_average


# 각 테이트 케이스에서 평균을 넘는 학생의 비율을 구하는 함수
def over_average():
    global test_average
    for i in range(0, C):
        student_num = test_list[i][0]
        student_count = 0
        for j in range(1, student_num+1):
            if test_list[i][j] > test_average[i]:
                student_count += 1
        student_over_average = (student_count / student_num) * 100
        print('{:.3f}%'.format(student_over_average))


average()
over_average()
