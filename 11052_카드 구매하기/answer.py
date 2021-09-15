import sys
sys.stdin = open('input.txt')

# dp[1] 은 카드를 1개 쓰는 방법으로 1가지 뿐
# dp[2] 는 카드를 2개 쓰는 건데, 1개를 두번 쓰거나 두 개의 카드를 쓰거나
# dp[3] 는 카드 1개 * 3 , 카드 2개, 카드 3개 * 1

N = int(input())
card = [0]
card += list(map(int, input().split()))
print(card)
dp = [0] * (N+1)
dp[1] = card[1]
dp[2] = max(card[2], card[1] * 2)
print(dp)

for i in range(3, N+1):
    dp[i] = card[i]
    for j in range(1, i//2 + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])