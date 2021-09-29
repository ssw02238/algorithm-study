import sys
sys.stdin = open('input.txt')

T = int(input())

def binary(num):

    start, end = 0, N-1
    if start == end and note1[start] == num:
        return 1
    elif start == end and note1[start] != num:
        return 0
    target = note1[(start+end) // 2]

    while start < end:
        target = note1[(start+end)//2]
        if target == num:
            return 1

        if target < num:
            start = (start+end)//2
        elif target > num:
            end = (start+end)//2
        if end-start == 1:
            if note1[start] != num and note1[end]!= num:
                return 0
            else:
                return 1


for tc in range(1, T+1):
    N = int(input())
    note1 = list(map(int, input().split()))
    note1.sort() # [1, 2, 3, 4, 5]
    M = int(input())
    note2 = list(map(int, input().split()))

    for i in range(M):
        print(binary(note2[i]))
