import sys
sys.stdin = open('input.txt')


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# 산봉우리 찾기
def solution(x, y):
    dx = [0,0,-1,1]
    dy = [-1, 1, 0, 0]



for i in range(n):
    for j in range(m):
        