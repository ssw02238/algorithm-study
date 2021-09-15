import sys
sys.stdin = open('input.txt')


N = int(input())
cards = list(map(int, input().split()))
idx = [i for i in range(1, N+1)]
print(idx)
result = 0
# idx로 먼저 부분집합의 합이 N 인 그룹들 구하기
for i in range(1 << N):
    subset = []
    sum_v = 0
    price = 0
    for j in range(N):
        if i & (1 << j):
            subset.append(idx[j])
            sum_v += idx[j]
    # print(subset)
    if sum_v == N:
    # 그리고 그 부분집합 원소들의 가격들을 더하기
        print(subset)
        for k in range(len(subset)):
            price += cards[subset[k]-1]
        if price > result:
            result = price
        print(result)
print(result)