import sys
sys.stdin = open('input.txt')

people = int(input()) # 사람 수
a, b = map(int, input().split())

N = int(input())  # 관계의 수

result = [0] * (people+1)
Matrix = [[] for i in range(people+1)]
for i in range(N):
  x, y  = map(int, input().split())
  # 양방향으로 값 넣음
  Matrix[x].append(y)
  Matrix[y].append(x)

def BFS(start, end):
    queue = [start]
    visit = []
    while queue:
        point = queue.pop(0)
        visit.append(point)   # 방문 체크

        if point == end:
            break
        for i in Matrix[point]:
            if i not in visit:
                result[i] = result[point] + 1
                queue.append(i)
    if result[end] == 0:
        print(-1)
    else:
        print(result[end])
BFS(a, b)