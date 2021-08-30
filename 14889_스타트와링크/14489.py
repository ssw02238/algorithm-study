import sys
sys.stdin = open('input.txt')

N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]

gap = 99999999999999999999999

# dfs 로 탐색
def dfs(idx, cnt):
    global gap
    if cnt == N // 2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if select[i] and select[j]:
                    start += synergy[i][j]
                elif not select[i] and not select[j]:
                    link += synergy[i][j]
        gap = min(gap, abs(start-link))

    for i in range(idx, N):
        if select[i]:
            continue
        select[i] = 1
        dfs(i+1, cnt +1)
        select[i] = 0


# 팀 선발
select = [0 for _ in range(N)]
dfs(0, 0)
print(gap)