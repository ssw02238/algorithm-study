import sys
sys.stdin = open('input.txt')

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()
result = 0
for i in range(N):
    result += A[i] * B[N-i-1]

print(result)
