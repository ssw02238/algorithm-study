from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'R':
            redx, redy = i, j
        elif matrix[i][j] == 'B':
            bluex, bluey = i, j


# 이동
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def solution(redx, redy, bluex, bluey):
    q = deque()
    q.append((redx, redy, bluex, bluey))
    visited = []
    visited.append((redx, redy, bluex, bluey))

    answer = 0

    while q:
        for _ in range(len(q)):
            redx, redy, bluex, bluey = q.popleft()
            if answer > 10:
                return -1
            if matrix[redx][redy] == 'O':
                return answer

            # 4방향 탐색
            for i in range(4):
                nrx, nry = redx, redy
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if matrix[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if matrix[nrx][nry] == 'O':
                        break

                nbx, nby = bluex, bluey
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if matrix[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if matrix[nbx][nby] == 'O':
                        break
                 # 만약 파란 구슬이 먼저 들어가면 스탐
                if matrix[nbx][nby] == 'O':
                    continue
                # 동시 들어가도 스탑
                # 더 많이 이동한 구슬이 더 늦게 이동한 구슬이므로 늦게 이동한 구슬 한칸 뒤로 이동
                if nrx == nbx and nry == nby:
                    if abs(nrx - redx) + abs(nry - redy) > abs(nbx - bluex) + abs(nby - bluey):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
            answer += 1
        return -1
print(solution(redx, redy, bluex, bluey))
