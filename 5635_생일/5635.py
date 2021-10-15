import sys
sys.stdin = open('input.txt')

N = int(input())
student = []
for i in range(N):
    info = input().split()
    info[1] = int(info[1])
    info[2] = int(info[2])
    info[3] = int(info[3])
    student.append(info)

student.sort(key = lambda x:(x[3], x[2], x[1]))

print(student[-1][0])
print(student[0][0])