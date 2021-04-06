import sys
input = sys.stdin.readline

a,b = input().strip().split()
a,b = int(a[::-1]), int(b[::-1])

if a > b : print(a)
else : print(b)