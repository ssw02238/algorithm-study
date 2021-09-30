import sys
sys.stdin = open('input.txt')


N1, N2 = map(int, input().split())
group1 = list(input())
group2 = list(input())
T = int(input())



time = 0
result = []
# 0번 direction
for i in range(N1-1, -1, -1):
    result.append([group1[i],0])
# 1번 direction
for i in range(N2):
    result.append([group2[i], 1])
# [['C', 0], ['B', 0], ['A', 0], ['D', 1], ['E', 1], ['F', 1]]

visit = [False for _ in range(len(result))]
while time != T:
    for i in range(len(result)-1):
        if result[i][1] == 0 and result[i+1][1] == 1 and not visit[i] and not visit[i+1]:
            result[i], result[i+1] = result[i+1], result[i]
            visit[i], visit[i+1] = True, True
    time += 1
    visit = [False for _ in range(len(result))]


for i in range(len(result)):
    print(result[i][0], end='')