import sys
sys.stdin = open('input.txt')

N = int(input())
squares = [list(map(int, input().split())) for _ in range(N)]

# [[2, 4], [4, 6], [5, 3], [8, 10], [11, 4], [13, 6], [15, 8]]
answer = 0
squares.sort(key = lambda x : x[0])


idx = 0
cnt = 1
while idx != N:
    L, H = squares[idx][0], squares[idx][1]
    if idx == N-1:
        idx += 1
        break
    elif (idx + cnt) == N - 1:
        answer += (squares[idx+cnt][0] - L ) * squares[idx+cnt][1]
        answer += H
        break
    else:
        # 다음 창고가 더 높을 때
        if squares[idx+cnt][1] > H:
            answer += (squares[idx+cnt][0] - L) * H
            idx += cnt
            cnt = 1
        # 다음 창고가 더 낮을 때
        else:
            cnt += 1

print(answer)