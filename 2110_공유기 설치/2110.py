import sys
sys.stdin = open('input.txt')

from itertools import combinations

N, C = map(int, input().split())
wifi = list(int(input()) for _ in range(N))
# wifi = [1, 2, 8, 4, 9]

wifi.sort()

def solution(wifi, C):
    if N == 2:
        distance = wifi[1] - wifi[0]
        return distance
    pick = list(combinations(wifi[1:len(wifi)-1], C-2))
    # print(pick)
    distance = 0
    for i in range(len(pick)):
        target = list(pick[i])
        target.append(wifi[0])
        target.append(wifi[-1])
        # print(target)
        target.sort()
        gap_a = target[1] - target[0]
        gap_b = target[-1] - target[-2]
        if distance < min(gap_a, gap_b):
            distance = min(gap_a, gap_b)
    return distance

print(solution(wifi, C))
