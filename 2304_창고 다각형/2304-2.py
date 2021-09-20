import sys
sys.stdin = open('input.txt')

from collections import Counter

N = int(input())
squares = [list(map(int, input().split())) for _ in range(N)]
squares.sort(key=lambda x:x[0]) # x 축 순서로 정렬

max_h = max(squares, key=lambda x:x[1])[1]
# 해당 높이를 가진 기둥의 개수를 구하고 그게 0이 될 것을 기준으로
h_cnt = Counter(list(zip(*squares))[1])
max_h_cnt = h_cnt[max_h]
answer = 0
x, y = squares[0][0], 0

for i in range(len(squares)):
    square = squares[i]
    if max_h_cnt > 0: # 높이가 제일 높은게 2개 이상이라면
        if square[1] >= y:
            answer += (square[0] - x) * y
            x, y = square[0], square[1] # 갱신
        if square[1] == max_h:
            answer += y # 본인의 넓이만 더함
            x += 1 # x 갱신
            max_h_cnt -= 1 # 제일 높은 기둥의 개수를 줄임
    else:
        max_h = max(squares[i:], key=lambda x: x[1])[1] # 매번 정렬하면서 높이 파악
        if max_h == square[1]:
            y = square[1]
            answer += (square[0] - x + 1) * y
            x = square[0] + 1
print(answer)
