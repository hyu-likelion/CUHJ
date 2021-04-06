#문제7
cnt = int(input())
for i in range(cnt) :
    case = input()
    case = case.split()
    n = int(case.pop(0))
    scores = list(map(int, case))
    total = 0
    ratio = 0

    for score in scores :
        total = total + score
        avg = total/n

    for score in scores :
        if score > avg :
            ratio = ratio+1
            
    print(str('%0.3f'%(ratio/n*100))+"%")
