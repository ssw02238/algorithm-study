import sys
sys.stdin = open('input.txt')

from itertools import permutations
N, K = map(int, input().split())
exercises = list(map(int, input().split()))
l = len(exercises)

lst = list(permutations(exercises, l))


result = 0

def solution(i):
    global result
    weight = 500
    for j in range(l):
        weight += lst[i][j]
        weight -= K
        if weight < 500:
            return
    result += 1

for i in range(len(lst)):
    solution(i)
print(result)