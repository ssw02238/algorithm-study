# S: 직진
# L: 좌회전
# R: 우회전
import sys
sys.stdin = open('input.txt')

# 1. 입력 받은거 slice 해서 리스트에 저장
temp = input()[1:-1]
grid = []
idx = [] # 반점 기준으로 SLICING
slice_idx = 0   # 반점 자를 시작 지점
for i in range(len(temp)):
    if temp[i] == ',':
        idx.append(i)
        grid.append(list(temp[slice_idx+1:i-1]))
        slice_idx = i + 1
grid.append(list(temp[slice_idx+1:-1]))
# grid = [['S', 'L'], ['L', 'R']]

start = (0,0)
visit = []
dir = ['L', 'R', 'S']
# 2. 경로 누적 (참고)
def solution(grid):
    global visit
    for i in range(4):
        for j in range(4):
            for dir in range(3):
                if not visit[i][j][dir]:
                    x, y, z = i, j, dir

print(solution(grid))



