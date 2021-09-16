import sys
from collections import deque

def bfs(x):
    global leaf
    visited[x] = 1
    q = deque()
    q.append(x)
    while q:
        n = q.popleft()
        # len이 1이라는 것은 부모만 있다는 이야기
        if len(graph[n]) == 1 and visited[graph[n][0]]:
            # 말단에 있는 잎의 개수를 센다
            leaf += 1
        for i in graph[n]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)


N, W = map(int, sys.stdin.readline().split())
visited = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
leaf = 0
bfs(1)
print(W/leaf)