key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 0은 홈 부분, 1은 돌기 부분

def rotation(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            ret[j][n-1-i] = arr[i][j]
    return ret

def check(startX, startY, key, lock, expendList, start, end):
    expendArr = [[0] * expendList for _ in range(expendList)]

    for i in range(len(key)):
        for j in range(len(key)):
            expendArr[startX + i][startY + j] += key[i][j]
    for i in range(start, end):
        for j in range(start, end):
            expendArr[i][j] += lock[i - start][j - start]
            if expendArr[i][j] != 1:
                return False

def solution(key, lock):
    start = len(key) - 1
    end = start + len(lock)
    expendList = len(lock) + start * 2

    for a in range(0, 4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expendList, start, end):
                    return True
        key = rotation(key)
    return False