import sys
sys.stdin = open('input.txt')

N = int(input())
squares = [list(map(int, input().split())) for _ in range(N)]

# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
answer = 0
squares.sort(key = lambda x : x[0])
min_x = squares[0][0]
max_x = squares[-1][0]
visit = [False for _ in range(0, max_x+2)]

squares.sort(key=lambda x:-x[1])
print(squares)

# 높이 순으로 나열
# 제일 높은 거와 다음 높은 거를 target1, target2 로 설정
target1, target2 = squares[0], squares[1]
print(target1, target2)
# 제일 높은거 본인 넓이도 더하기
if target1[1] > target2[1]:
    answer += (target1[1] + (target2[0] - target1[0]) * target2[1])
elif target1[1] == target2[1]:
    answer += (target2[0] - target1[0]) * target1[1]
# 그 사이에 x 좌표는 모두 visit 표시
for i in range(target1[0], target2[0]+2):
    visit[i] = True
# 다음 높은거 visit 확인하고 target1, target2 중 가까운거 찾기

# 이젠 더 작은 애니까 target의 x 좌표랑 다음 타자 x 좌표 뺀거랑 더 작은 y축 곱하기
# 그 사이 x 값들 다 visit 표시
# target1, 2 갱신
# 반복
