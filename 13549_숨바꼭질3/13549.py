N = 5
K = 17

def solution(N, K):
    # 01 순간이동을 초기 세팅
    # 동생이 더 앞에 있을 때
    if N < K:
        start = N
        while True:
            if start <= K <= start * 2:
                gap_a = K - start
                gap_b = start * 2 - K
                if gap_a <= gap_b:
                    N = start
                else:
                    N = start * 2
                break
            else:
                start = 2 * start
    elif N == K:
        return 0
    # 동생이 더 뒤에 있을 때
    else:
        start = N
        while True:
            if (start // 2) + 1 <= K <= start:
                gap_a = K - (start//2+1)
                gap_b = start - K
                if gap_a <= gap_b:
                    N = start // 2 + 1
                else:
                    N = start
                break
            else:
                start = N // 2 + 1

    # 02 한 칸 씩 이동으로 찾기
    time = abs(N-K)
    return time

print(solution(N, K))
