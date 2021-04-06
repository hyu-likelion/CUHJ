#문제2
num = int(input())
for i in range(1, num+1) :
    if num < 1:
        break
    elif num > 100 :
        break
    else :
        print("*"*i)
        i =+ 1
