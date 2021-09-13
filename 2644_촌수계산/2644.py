import sys
sys.stdin = open('input.txt')

people = int(input())
x, y = map(int, input().split()) # 7 3
if x > y:
    person1 = x
    person2 = y
else:
    person1 = y
    person2 = x

N = int(input())
parents = [[] for i in range(people+1)]
children = [[] for i in range(people+1)]

for i in range(N):
    x, y = map(int, input().split())
    parents[x].append(y) # 엄마 index에 자식 넣기 [[], [2, 3], [7, 8, 9], [], [5, 6], [], [], [], [], []]
    children[y].append(x) # 자식 index에 엄마 넣기 [[], [], [1], [1], [], [4], [4], [2], [2], [2]]
cnt = 0

def solution(person1, person2):
    global cnt
    if children[person1]:
        cnt += 10
        parent = children[person1][0]
        if parent == person2:
            return cnt
    else:
        cnt =  -1
        return cnt
    if person2 in parents[parent]:
        cnt += 1
        return cnt
    solution(parent, person2)
    if cnt == -1:
        return cnt
    return cnt


print(solution(person1, person2))


