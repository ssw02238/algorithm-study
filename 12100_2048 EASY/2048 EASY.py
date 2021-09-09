# 값만 복사해오는 deepcopy 이용!!! (게임으로 움질일 동안 초기 틀은 깨지면 안돼)
import sys, copy
input = sys.stdin.readline

# 이동시키는 함수
def move(dir):
    # 상
    if dir == 0:
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if game[j][i]:
                    temp = game[j][i]
                    # 이동 후 0으로 리셋
                    game[j][i] = 0
                    if game[idx][i] == 0:
                        # 그대로
                        game[idx][i] = temp
                    # 같을 경우 더해짐
                    elif game[idx][i] == temp:
                        game[idx][i] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        # 그대로
                        game[idx][i] = temp
    # 하
    elif dir == 1:
        for j in range(N):
            idx = N - 1
            for i in range(N - 2, -1, -1):
                if game[i][j]:
                    temp = game[i][j]
                    game[i][j] = 0
                    if game[idx][j] == 0:
                        game[idx][j] = temp
                    elif game[idx][j] == temp:
                        game[idx][j] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        game[idx][j] = temp
    elif dir == 2:
        for i in range(N):
            idx = 0
            for j in range(1, N):
                if game[i][j]:
                    temp = game[i][j]
                    game[i][j] = 0
                    if game[i][idx] == 0:
                        game[i][idx] = temp
                    elif game[i][idx] == temp:
                        game[i][idx] = temp * 2
                        idx += 1
                    else:
                        idx += 1
                        game[i][idx] = temp
    else:
        for i in range(N):
            idx = N - 1
            for j in range(N - 2, -1, -1):
                if game[i][j]:
                    temp = game[i][j]
                    game[i][j] = 0
                    if game[i][idx] == 0:
                        game[i][idx] = temp
                    elif game[i][idx] == temp:
                        game[i][idx] = temp * 2
                        idx -= 1
                    else:
                        idx -= 1
                        game[i][idx] = temp

# 이동 횟수 카운트 함수
def dfs(cnt):
    global game, result
    if cnt == 5:
        # 최댓값 비교
        for i in range(N):
            for j in range(N):
                result = max(result, game[i][j])
        return

    # 아직 5번이 안 됐다면 계속 이동
    temp_game = copy.deepcopy(game)
    # 네 방향으로 보내버림 (0, 1, 2, 3)
    for i in range(4):
        move(i)
        dfs(cnt + 1)
        game = copy.deepcopy(temp_game)

N = int(input())
game = [list(map(int, input().split())) for _ in range(N)]
result = 0
dfs(0)
print(result)