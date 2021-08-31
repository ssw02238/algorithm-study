import sys
from itertools import combinations
sys.stdin = open('input.txt')

N, M = map(int, input().split())
info = [list(map(int, input().split()))for _ in range(N)]

# 치킨집 수를 M개에 맞춰야 한다
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if info[i][j] == 2:
            chicken.append([i, j])
        elif info[i][j] == 1:
            house.append([i, j])


distance = 999999999999
for case in combinations(chicken, M):
    mini_distance = 0
    for home in house:
        mini_distance += min([abs(home[0] - store[0]) + abs(home[1]-store[1]) for store in case])
        if mini_distance >= distance:
            break
    if mini_distance < distance:
        distance = mini_distance
print(distance)


