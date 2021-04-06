import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    L = list(map(int, input().split()))
    avg = sum(L[1:])/L[0]  
    cnt = 0
    for score in L[1:]:
        if score > avg:
            cnt += 1  
    rate = cnt/L[0] *100
    print(f'{rate:.3f}%')