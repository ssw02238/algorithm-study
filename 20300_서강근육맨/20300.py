import sys
sys.stdin = open('input.txt')

N = int(input())
lose = list(map(int, input().split()))
lose.sort()
print(lose)

# 1. 짝수 일때는 정렬하여 0, N-1 번째 합
if N % 2 == 0:
    result = 0
    for i in range(N//2):
        if lose[i] + lose[N-i-1] > result:
            result = lose[i] + lose[N-i-1]
else:
# 2. 홀수 일때는 0, N번째 합
    result = lose[-1]
    for i in range((N-1)//2):
        if lose[i] + lose[N - i - 2] > result:
            result = lose[i] + lose[N - i - 2]

print(result)