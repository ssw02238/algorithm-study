def solution(n, t, m, p):
    def get_change(number, n):
        arr = "0123456789ABCDEF"  # 16진법까지 가능하게
        q, r = divmod(number, n)
        if q == 0:
            return arr[r]
        else:
            return get_change(q, n) + arr[r]


    answer = ''
    numbers = []
    for i in range(t*m):
        number = get_change(i, n)
        for num in number:
            numbers.append(num)

    for i in range(t):
        answer += numbers[p-1+i*m]
    print(answer)

solution(2, 4, 2, 1)



