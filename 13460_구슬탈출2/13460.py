import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
# [['#', '#', '#', '#', '#'], ['#', '.', '.', 'B', '#'], ['#', '.', '#', '.', '#'], ['#', 'R', 'O', '.', '#'], ['#', '#', '#', '#', '#']]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'R':
            red = [i, j]
            queueR = [(i, j)]
        elif matrix[i][j] == 'B':
            blue = [i, j]
            queueB = [(i, j)]
        elif matrix[i][j] == 'O':
            hole = [i, j]
print(queueR, queueB)

answer = 0
def solution(matrix, answer):
    global answer
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 여기서 같이 동반자로 간 다음에 체크해야 했음 ㅠ
    while queueR:
        rsx, rsy = queueR[0][0], queueR[0][1]
        if matrix[rsy][rsx] == 'O':
            return answer

        bsx, bsy = queueB[0][0], queueB[0][1]
        queueR.pop()
        queueB.pop()
        for i in range(4):
            rnx, rny = rsx + dx[i], rsy + dy[i]
            bnx, bny = bsx + dx[i], bsy + dy[i]
            if matrix[rny][rnx] == '#':
                pass
                if matrix[bny][bnx] == '.':

            elif matrix[rny][rnx] == '.':
                queueR.append((rny, rnx))
                solution(matrix, answer +1)











print(solution(matrix,0))


