import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
answer = 0

while bin(n).count('1') > k:
    semi = 2 ** (bin(n)[::-1].index('1'))
    answer += semi
    n += semi
print(answer)