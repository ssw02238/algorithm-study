import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    stations = list(map(int, input().split()))

    idx = len(stations) // 2
    # 절반을 나눠서 두 그룹을 형성해야 함
    first = stations[: idx]
    second = stations[idx:]

    # 2개 선발
    first_result = 0
    first_visit = []
    for i in range(len(first)-2):
        pick_1 = first[i]
        for j in range(i+2, len(first)):
            pick_2 = first[j]
            result = pick_1**2 + pick_2**2
            if result > first_result:
                visit = [0 for _ in range(len(first)+1)]
                visit[i] = 1
                visit[j] = 1
                first_visit = visit
                first_result = result

    # first에서 0번째나 N-1번째가 포함되었을 때

    # 상관 없을 때
    second_result = 0
    second_visit = []
    for i in range(len(second) - 2):
        pick_1 = second[i]
        for j in range(i + 2, len(second)):
            pick_2 = second[j]
            result = pick_1 ** 2 + pick_2 ** 2
            if result > second_result:
                visit = [0 for _ in range(len(second) + 1)]
                visit[i] = 1
                visit[j] = 1
                second_visit = visit
                second_result = result
    print('#{} {}'.format(tc,first_result+second_result))