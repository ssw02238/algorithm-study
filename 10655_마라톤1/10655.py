import sys
sys.stdin = open('input.txt')

from copy import deepcopy

N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]

distance = 9999999999999999999999

for i in range(1, N-1):
    ppoint = point[i]
    point_pass = deepcopy(point)
    point_pass.remove(point_pass[i])

    result = 0
    for j in range(len(point_pass)-1):
        result += abs(point_pass[j][0] - point_pass[j+1][0]) + abs(point_pass[j][1] - point_pass[j+1][1])
    if result < distance:
        distance = result
print(distance)