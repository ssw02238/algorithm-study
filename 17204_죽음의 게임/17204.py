import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

call = list(int(input()) for _ in range(N))
# print(call) # [1, 3, 2, 1, 4]

cnt = 0
start = 0
while cnt< N:
    target = call[start]
    if target == K:
        cnt += 1
        print(cnt)
        break
    else:
        start = call[start]
        cnt += 1

if target != K and cnt == N:
    print(-1)