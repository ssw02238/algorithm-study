import sys
sys.stdin = open('input.txt')

N = int(input()) # 사진틀 개수
M = int(input()) # 전체 추천 횟수
recommend = list(map(int, input().split()))

pictures = []

for i in range(M):
    flag = False
    # 만약 사진첩에 이미 후보가 있다면
    if pictures:
        for j in range(len(pictures)):
            if pictures[j][0] == recommend[i]:
                pictures[j][1] += 1
                flag = True
                break

    if flag == False:
        # 사진첩에 후보가 없다면
        if len(pictures) < N:
            # 사진첩에 추가
            pictures.append([recommend[i], 1, i])
        # 사진첩이 꽉 찼다면
        else:
            pictures.sort(key=lambda x:(-x[1], -x[2]))
            pictures.pop(-1)
            pictures.append([recommend[i], 1, i])

pictures.sort(key=lambda x:x[0])
for i in range(len(pictures)):
    if i == N-1:
        print(pictures[i][0])
    else:
        print(pictures[i][0], end=' ')