import sys
sys.stdin = open('input.txt')

r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
visit = [[0] * c for _ in range(r)]

little_sheep, little_wolves = 0, 0
def dfs(i, j):
    global little_sheep, little_wolves
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for dir in range(4):
        nx = dx[dir] + i
        ny = dy[dir] + j
        if 0 <= nx < r and 0 <= ny < c:
            if not visit[nx][ny]:
                if matrix[nx][ny] == '#':
                    pass
                elif matrix[nx][ny] == '.':
                    visit[nx][ny] = 1
                    dfs(nx, ny)
                elif matrix[nx][ny] == 'o':
                    visit[nx][ny] = 1
                    little_sheep += 1
                    dfs(nx, ny)
                else:
                    visit[nx][ny] = 1
                    little_wolves += 1
                    dfs(nx, ny)

sheep, wolves = 0, 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'v' and not visit[i][j]:
            visit[i][j] = 1
            little_wolves += 1
            dfs(i, j)

            if little_sheep > little_wolves:
                sheep += little_sheep
            else:
                wolves += little_wolves

        elif matrix[i][j] == 'o' and not visit[i][j]:
            visit[i][j] = 1
            little_sheep += 1
            dfs(i, j)

            if little_sheep > little_wolves:
                sheep += little_sheep
            else:
                wolves += little_wolves
        little_wolves, little_sheep = 0, 0

print(sheep, wolves)