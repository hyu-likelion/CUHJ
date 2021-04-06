import sys
from collections import defaultdict
input = sys.stdin.readline

string = input().strip().lower()
alpha = defaultdict(int)
result = -1
ptr = ""

for c in string :
    alpha[c] += 1 
    if result < alpha[c] :
        result = alpha[c]

count = 0

for i in alpha :
    if alpha[i] == result :
        count += 1
        ptr = i
        if count == 2 :
            print('?')
            exit()

print(ptr.upper())