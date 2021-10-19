import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):

    N = int(input())
    boards = [list(map(int, input().split())) for _ in range(N)]
    # [[0, 1, 0, 0, 1], [1, 1, 0, 0, 0], [0, 1, 1, 0, 1], [0, 0, 2, 0, 0], [1, 0, 1, 1, 0]]

    for i in range(N):
        for j in range(N):
            if boards[i][j] == 2:
                p_x = i
                p_y = j
    # 포 초기 위치 3,2
    answer = 0
    def solution(p_x, p_y, boards, cnt):
        global answer
        dx = [0, 0, -1 ,1]
        dy = [1, -1, 0, 0]
        if cnt == 3:
            return
        for i in range(4):
            nx = p_x + dx[i]
            ny = p_y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if boards[nx][ny] == 1:
                    # 그 다음 칸은 범위만 허용된다면 바로 포 이동
                        nnx = nx + dx[i]
                        nny = ny + dy[i]
                        if 0 <= nnx < N and 0 <= nny < N:
                            if boards[nnx][nny] == 1:
                                answer += 1
                            boards[nnx][nny] = 2
                            boards[p_x][p_y] = 0
                            solution(nnx, nny, boards, cnt+1)
                else:
                    while 0 <= nx < N and 0 <= ny < N:
                        nx = nx + dx[i]
                        ny = ny + dy[i]
                        if boards[nx][ny] == 1:
                            if 0 <= nx < N and 0 <= ny < N:
                                if boards[nx][ny] == 1:
                                    answer += 1
                                boards[nx][ny] = 2
                                boards[p_x][p_y] = 0
                                solution(nx, ny, boards, cnt + 1)

    print('#{} {}'.format(tc, answer))