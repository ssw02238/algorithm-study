import sys
sys.stdin = open('input.txt')

import math
N = int(input())
drink = list(map(int, input().split()))
drink.sort()
drink.reverse()

result = drink[0]
for i in range(1, N):
    result += (drink[i] / 2)

print(math.trunc(result))