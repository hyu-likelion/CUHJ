#문제6 == 문제4
nums = input()
num1 = nums.split()[0]
num2 = nums.split()[1]

num1_rv = int(num1[::-1])
num2_rv = int(num2[::-1])

if num1_rv > num2_rv :
    print(num1_rv)
else :
    print(num2_rv)
