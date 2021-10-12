import sys
sys.stdin = open('input.txt')

w, h = map(int, input().split())
N = int(input())
position = [list(map(int, input().split())) for _ in range(N)]
xs, ys = map(int, input().split())

# 1북 2남 3서 4동

answer = 0
for i in range(N):
    dir, pos = position[i][0], position[i][1]
    # 반대 방향 일때
    if dir + xs == 3:
        if pos + ys < w - pos + w - ys:
            answer += (pos+ys+h)
        else:
            answer += (2*w - pos - ys + h)
    elif dir + xs == 7:
        if pos + ys < 2 * h - pos - ys:
            answer += (pos + ys)
        else:
            answer += (2 * h - pos - ys + w)
    elif dir + xs == 4:
        answer += (pos + ys)
    elif dir + xs == 6:
        answer += (h - )

