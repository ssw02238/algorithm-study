import sys
sys.stdin = open('input.txt')

n = int(input()) # n x n 격자
bomb = [list(input()) for _ in range(n)]
player =[list(input()) for _ in range(n)]


def count_bomb(i, j):
    dx = [0, 0, 1, -1, -1, -1, 1, 1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1]
    cnt = 0
    for dir in range(8):
        nx = i + dx[dir]
        ny = j + dy[dir]
        if 0 <= nx < n and 0 <= ny < n:
            # 주변에 bomb가 있다면
            if bomb[nx][ny] == '*':
                cnt += 1
            # 주변에 bomb가 없다면
            else:
                pass
    return cnt

flag = True
for i in range(n):
    if flag == True:
        for j in range(n):
            if player[i][j] == 'x':
                # 만약 지정한 위치가 바로 bomb라면
                if bomb[i][j] == '*':
                    player = bomb
                    flag = False
                    break
                else:
                    player[i][j] = count_bomb(i, j)

for i in range(n):
    for j in range(n):
        print(player[i][j], end='')
    print()
