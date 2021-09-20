import sys
sys.stdin = open('input.txt')

from itertools import combinations
import copy

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]


# [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]
# 01 0이 적힌 모든 위치를 리스트에 저장
zero_idx = []
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            zero_idx.append([i, j])

# 02 리스트에서 세 군데를 선택한다.
pick = list(combinations(zero_idx, 3))
answer = 0
# 03 matrix 돌면서 벽으로 세운다.
for i in range(len(pick)):
    result = 0
    x1, y1 = pick[i][0][0], pick[i][0][1]
    x2, y2 = pick[i][1][0], pick[i][1][1]
    x3, y3 = pick[i][2][0], pick[i][2][1]

    matrix_copy = copy.deepcopy(matrix)
    # 뽑힌 구간들 벽으로 교체
    matrix_copy[x1][y1] = 1
    matrix_copy[x2][y2] = 1
    matrix_copy[x3][y3] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for x in range(N):
        for y in range(M):
            if matrix_copy[x][y] == 0:
                cnt_virus = 0
                for dir in range(4):
                    nx = x + dx[dir]
                    ny = y + dy[dir]
                    if 0 <= nx < N and 0 <= ny < M:
                        if matrix_copy[nx][ny] == 2:
                            cnt_virus += 1
                # 근처에 하나라도 바이러스가 있다면
                if cnt_virus > 0:
                    matrix_copy[x][y] = 2
                # 여전히 0으로 남을 애들
                else:
                    result += 1
    if result > answer:
        answer = result
print(answer)
