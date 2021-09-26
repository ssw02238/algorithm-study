from collections import deque
import sys

# N, K = map(int, sys.stdin.readline().split())

N = 5
K = 17
# 좌표 이동시키면서 cnt를 저장할 리스트
arr = [-1] * 100001

q = deque()
q.append(N)
arr[N] = 0 # 시작점 찍기

while q:
    print(arr[10:20])
    start = q.popleft()
    if start == K:
        print(arr[N])
        break
    for num in (2*start, start-1, start+1):
        if 0 <= num < 100001 and arr[num] == -1:
            if num == 2 * start:
                arr[num] = arr[start]
                q.append(num)
            else:
                arr[num] = arr[start] + 1
                q.append(num)
