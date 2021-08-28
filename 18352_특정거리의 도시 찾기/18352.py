import sys
from collections import deque
input = sys.stdin.readline

# input 처리
N, M, K, X = map(int, input().split())
routes = [[] for _ in range(N)]
for i in range(M):
    start, end = map(int, input().split())
    routes[start].append(end)
# routes
# [[0], [0, 2, 3], [0, 3, 4], [0]]

# 변수 처리
result = []
visited = [False] * (N+1)

q = deque()
q.append((X, 0))
while q:
    node, cnt = q.popleft()
    if cnt == K:
        result.append(node)
    elif cnt < K:
        for path in routes[node]:
            if not visited[path]:
                visited[path] = True
                q.append((path, cnt + 1))
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for ans in result:
        print(ans)


