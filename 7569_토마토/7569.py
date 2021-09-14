import sys
sys.stdin = open('input.txt')

M, N , H = map(int, input().split())
tomatos = []
rotten = 0

done = []
visit = 0
for i in range(H):
    for j in range(N):
        tomato = list(map(int, input().split()))
        tomatos.append(tomato)
        if 0 in tomato:
            rotten += 1
        for j in range(M):
            if tomato[j] == 1:
                done.append([i, j, 0])
                visit += 1
            elif tomato[j] == -1:
                visit += 1

print(tomatos)


dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, 1]
def solution(tomatos):
    global visit
    while done:
        target = done.pop(0)
        x, y, days = target[0], target[1], target[2]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M:
                if tomatos[nx][ny] == 0:
                    visit += 1
                    tomatos[nx][ny] = 1
                    done.append([nx, ny, days+1])
        if visit == M*N:
            return days
    if visit != M*N:
        return -1
    return days


if rotten == 0:
    print(0)
else:
    print(solution(tomatos))





