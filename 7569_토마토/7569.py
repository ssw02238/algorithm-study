import sys
sys.stdin = open('input.txt')

M, N , H = map(int, input().split())
tomatos = [[list(map(int, input().split())) for i in range(N)] for depth in range(H)]


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, 1]

done = []
rotten = 1
visit = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            tomato = tomatos[i][j][k]
            if tomato == 1:
                done.append([i, j, k, 0])
                visit += 1
            elif tomato == -1:
                visit += 1
            else:
                rotten += 1

print(tomatos)

def solution(tomatos):
    global visit
    while done:
        target = done.pop(0)
        x, y, z, days = target[0], target[1], target[2], target[3]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H:
                if tomatos[nx][ny][nz] == 0:
                    visit += 1
                    tomatos[nx][ny][nz] = 1
                    done.append([nx, ny, nz, days+1])
        if visit == M*N:
            return days
    if visit != M*N:
        return -1
    return days


if rotten == 0:
    print(0)
else:
    print(solution(tomatos))





