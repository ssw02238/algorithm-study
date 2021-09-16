import sys
sys.stdin = open('input.txt')

N, L, R = map(int, input().split())
populations = [list(map(int, input().split())) for _ in range(N)]
# [[50, 30], [20, 40]]
visit = [[0 for i in range(N)] for _ in range(N)]
# [[0, 0], [0, 0]]
tree = list([[] for _ in range(N)] for _ in range(N))
print(tree)

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while True:
        tree = []
    for i in range(N):
        for j in range(N):
            target = populations[i][j]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < N:
                    gap = abs(target - populations[nx][ny])
                    if L <= gap <= R:
                        tree[i][j].append([nx, ny])
    for i in range(N):
        for j in range(N):
            target = tree[i][j]
            for k in range(len(target)):
                m, n = target[k][0], target[k][1]
                visit[m][n] = 1

dfs(0, 0)
