import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(par, com):
    tmp_par = defaultdict(int)

    for p in par :
        tmp_par[p] += 1

    for c in com :
        tmp_par[c] -= 1

    for i in tmp_par :
        if tmp_par[i] != 0 :
            return i


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["mislav"], []))
print(solution(["mislav", "mislav", "mislav"], ["mislav"]))
	


