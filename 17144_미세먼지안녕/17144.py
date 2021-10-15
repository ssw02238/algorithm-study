import sys

# 세로, 가로, 초(반복 횟수)
R, C, T = map(int, sys.stdin.readline().split(" "))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 인풋으로 들어오는 배열 채우기
field = []
for _ in range(R):
    field.append(list(map(int, sys.stdin.readline().split(" "))))

# 공기청정기 위치 찾기 (i와 i+1의 0번째 값이 공기청정기)
for i in range(R):
    if field[i][0] == -1 and field[i+1][0] == -1:
        purifier = [i, i+1]
        break

for _ in range(T):
    new = [[0 for _ in range(C) for _ in range(R)]]
    for i in range(R):
        for j in range(C):

            # 미세먼지 5 이상인 것만 취급
            if field[i][j] >= 5:
                # 나눠줄 양이랑 나눠줄 횟수
                each = field[i][j] // 5
                cnt = 0

                for k in range(4):
                    ndr, ndc = i + dr[k], j + dc[k]
                    if 0 <= ndr < R and 0 <= ndc < C and field[ndr][ndc] != -1:
                        cnt += 1
                        new[ndr][ndc] += each
                field[i][j] = field[i][j] - cnt * each


    for i in range(R):
        for j in range(C):
            field[i][j] += new[i][j]
    #######여기 까지는 불순 공기의 확장

    tmp = field[purifier[0]][C-1]
    for i in range(C-2, 0, -1):
        field[purifier[0]][i+1] = field[purifier[0]][i]
    tmp2 = field[0][C-1]
    for i in range(purifier[0]-1):
        field[i][C-1] = field[i+1][C-1]
    field[purifier[0]-1][C-1] = tmp

    tmp = field[0][0]
    for i in range(C-1):
        field[0][i] = field[0][i+1]
    field[0][C-2] = tmp2

    for i in range(purifier[0]-1, 1, -1):
        field[i][0] = field[i-1][0]
    field[purifier[0]][1] = 0
    field[1][0] = tmp

    temp = field[purifier[1]][C - 1]
    for i in range(C - 2, 0, -1):
        field[purifier[1]][i + 1] = field[purifier[1]][i]

    temp2 = field[R - 1][C - 1]
    for i in range(R - 1, purifier[1], -1):
        field[i][C - 1] = field[i - 1][C - 1]
    field[purifier[1] + 1][C - 1] = temp

    temp = field[R - 1][0]
    for i in range(C - 1):
        field[R - 1][i] = field[R - 1][i + 1]
    field[R - 1][C - 2] = temp2

    for i in range(purifier[1] + 1, R - 1):
        field[i][0] = field[i + 1][0]
    field[purifier[1]][1] = 0
    field[R - 2][0] = temp

# 남은 미세먼지 수 계산
s = 0
for each in field:
    s += sum(each)

# 공기청정기 2칸을 각각  -1로 표현했으니 최종값에 2를 더해줌
print(s + 2)