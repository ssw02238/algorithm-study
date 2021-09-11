import sys
sys.stdin = open('input.txt')

N = int(input())

trees = [list(map(int, input().split())) for _ in range(N-1)]
parents = [[] for _ in range(N+1)]
check = [0 for _ in range(N)]
print(check)
que = []

def solution(node):
    for i in range(N-1):
        if node in trees[i] and not check[i]:
            a, b = trees[i][0], trees[i][1]
            if a == node:
                parents[node].append(b)
                que.append(b)
            else:
                parents[node].append(a)
                que.append(a)
            check[i] = 1
    if que:
        a = que.pop(0)
        solution(a)
    else:
        return parents

solution(1)

for i in range(2, N+1):
    for j in range(1, N):
        if i in parents[j]:
            print(j)
