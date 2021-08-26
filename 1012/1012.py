import sys
sys.stdin = open('input.txt')

import sys
sys.setrecursionlimit(100000)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(matrix, y, x):
    matrix[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and matrix[ny][nx] == 1:
            solution(matrix, ny, nx)


T = int(input())
for i in range(1, T+1):
    # M 가로 // N 세로 // K 배추 위치 개수
    M, N, K = map(int, input().split())
    # matrix 배열 만들어 두기
    matrix = [[0] * M for _ in range(N)]
    for j in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1
    # 세팅 완료
    answer = 0
    for y in range(N):
        for x in range(M):
            if matrix[y][x] == 1:
                solution(matrix, y, x)
                answer += 1

    print(answer)