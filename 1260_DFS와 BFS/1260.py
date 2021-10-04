import sys
sys.stdin = open('input.txt')

N, M, V = map(int, input().split())
relations = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    relations[a].append(b)
    relations[b].append(a)

for i in range(N+1):
    relations[i].sort()

dfs_lst = [V]
def dfs(v):
    for i in range(len(relations[v])):
        a = relations[v][i]
        if a not in dfs_lst:
            dfs_lst.append(a)
            dfs(a)
    return dfs_lst

queue = [V]
bfs_lst = []
def bfs(v):
    for number in relations[v]:
        if number not in bfs_lst:
            queue.append(number)
    while queue:
        a = queue[0]
        if a not in bfs_lst:
            bfs_lst.append(a)
        bfs(queue.pop(0))
    return bfs_lst

print(*dfs(V))
print(*bfs(V))