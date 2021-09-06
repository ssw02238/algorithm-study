import sys
sys.stdin = open('input.txt')

N = int(input())
time_pay = []
optimize = []

for i in range(N):
    time_pay.append(list(map(int, input().split())))
    # 최적화 리스트에 일단 해당 날짜의 수당을 입력해 둠
    optimize.append(time_pay[-1][1])
optimize.append(0)
for i in range(N -1, -1, -1):
    # 만약 해당 일에서 걸릴 날짜를 더한 이후 범위를 벗어난다면
    if time_pay[i][0] + i > N:
        # 내 앞 날짜랑 pay가 같은 상태
        optimize[i] = optimize[i+1]
    else:
        optimize[i] = max(optimize[i+1], time_pay[i][1] + optimize[time_pay[i][0] + i])
print(max(optimize))

