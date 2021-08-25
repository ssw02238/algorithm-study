import sys
sys.stdin = open('input.txt')

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def solution(matrix):
    for i in range(N):
        for j in range(M):


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

    print(solution(matrix))