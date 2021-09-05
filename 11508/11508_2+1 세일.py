import sys
sys.stdin = open('input.txt')


N = int(input())
prices = [int(input()) for _ in range(N)]

answer = 0
prices.sort()
free = N // 3
answer = sum(prices)
for i in range(free):
    answer -= prices[(i+1)*-3]
print(answer)





# answer = sum(prices)
# for i in range(free):
#     answer -= prices[i]
# print(answer)
