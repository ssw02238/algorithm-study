import sys
input = sys.stdin.readline
import copy

# 문제 이해: A -> B (B 해킹 시 A 도 가능) - DP를 써야 하는지??????
N, M = map(int, input().split())
result = []
lst = [[] for i in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    lst[b].append(a)

# 각 인덱스 별로 해킹 가능한 컴퓨터 수 저장 리스트
cntlst = [0]
for i in range(1, N+1):
    queue = copy.deepcopy(lst[i])
    visit = [False] * (N+1)
    for j in range(len(lst[i])):
        visit[lst[i][j]] = True
    cnt = len(lst[i])
    while queue:
        point = queue.pop(0)
        for tmp in lst[point]:
            if not visit[tmp]:
                cnt += 1
                visit[tmp] = True
                queue.append(tmp)
    cntlst.append(cnt)

answer = max(cntlst)
cntlst.sort(reverse=True)
for i in range(len(cntlst)):
    if cntlst[i] == answer:
        print(i+1, end=' ')