n = 2
t = 4
m = 2
p = 1

def solution(n, t, m, p):
    def get_change(number, n):
        arr = "0123456789ABCDEF"  # 16진법까지 가능학 ㅔ
        q, r = divmod(number, n)
        if q == 0:
            return arr[r]
        else:
            return get_change(q, n) + arr[r]


    numbers = []
    cnt = 0

    # 1. 진행될 숫자 행렬을 쭉 나열
    while cnt < m*t:    # 튜브가 채워 놓을 숫자 회차까지 다 구해놓기
        if cnt >= 10:
            length = len(str(cnt))
            for i in range(length):
                numbers.append(str(cnt)[i])
        else:
            numbers.append(str(cnt))
        cnt += 1
    # print(numbers)

    # 2. n 진수로 변경
    change = []
    for i in range(len(numbers)):
        number = int(numbers[i])
        result = get_change(number, n)

        for num in result:
            change.append(num)
    # print(change)

    # 3. 튜브의 순서 때 마다 말할 수 구하기
    answer = ''
    for i in range(t):
        answer += change[p-1+i*m]
    print(answer)
    # 4. 출력

print(solution(n, t, m, p))
