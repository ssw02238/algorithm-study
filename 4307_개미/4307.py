import sys
sys.stdin = open('input.txt')

TC = int(input())
L, n = map(int, input().split()) # 막대 길이, 개미 수
position = []

for i in range(n):
    num = int(input())
    position.append(num)
min_result = 0
max_result = 0
for ant in position:
    # 다리 중심에서 오른쪽에 위치
    if ant > L - ant:
        if min_result < L - ant:
            min_result = L-ant
        if max_result < ant:
            max_result = ant
    # 다리 중심에서 왼쪽 위치
    else:
        if min_result < ant:
            min_result = ant
        if max_result < L-ant:
            max_result = L - ant
print(min_result, max_result)