

def solution(n):
    mem = [-1 for i in range(60001)]

    def dp(n):
        if mem[n] != -1:
            return mem[n]
        if n == 0:
            return 1
        if n == 1:
            return 1
        mem[n] = (dp(n-1) + dp(n-2)) % 1000000007
        return mem[n]
    return dp(n)



print(solution(n))