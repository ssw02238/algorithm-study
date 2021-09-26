import sys
sys.stdin = open('input.txt')

N, M, T = map(int, input().split())

# 0 빈곳, 1 벽, 2 그람
# 출발점 (0,0) 도착점 (N, M)

castle = [list(map(int, input().split())) for _ in range(N)]

start = [0, 0]
castle[0][0] = 1
# 걸리는 시간 비교
result = [-1]

def dfs(start, cnt):
    global result
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 공주 도착 시
    if start[0] == N-1 and start[1] == M-1:
        if cnt <= T:
            result.append(cnt)
            return

    for i in range(4):
        nx = start[0] + dx[i]
        ny = start[1] + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if castle[nx][ny] == 0:
                start = [nx, ny]
                castle[nx][ny] = 1
                dfs(start, cnt+1)
                castle[nx][ny] = 0
                start = [nx- dx[i], ny-dy[i]]
            elif castle[nx][ny] == 2:
                start = [nx, ny]
                cnt += (M-1) - nx + (N-1) - ny
                if cnt <= T:
                    result.append(cnt)
                    return
    return result


dfs(start, 0)

result.sort
if result[-1] == -1:
    print('Fail')
else:
    print(result[-1])
