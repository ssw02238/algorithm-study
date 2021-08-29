import sys
sys.stdin = open('input.txt')

candidate = []
N = int(input())
for i in range(N):
    a = input()
    total = 0
    for j in range(len(a)):
        if a[j].isdigit():
            total += int(a[j])
    candidate.append([a, len(a), total])
candidate.sort(key=lambda x:(x[1], x[2], x[0]))

for i in range(N):
    print(candidate[i][0])


