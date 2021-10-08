import sys
sys.stdin = open('input.txt')

S = input()
T = input()

result = 0
queue = [S]
tmp = S
while queue and len(tmp) <= len(T):
    tmp = queue.pop(0)
    # 규칙 1
    a = tmp + 'A'
    # 규칙 2
    b = list(reversed(list(tmp)))
    b.append('B')
    b1 = ''.join(b)

    # 확인
    if a == T or b1 == T:
        result = 1
        break
    else:
        ar = list(a)
        ar.reverse()
        ar = ''.join(ar)

        br = list(b1)
        br.reverse()
        br = ''.join(br)
        # print(ar, br)

        if a in T or ar in T:
            queue.append(a)
        if b1 in T or br in T:
            queue.append(b1)
print(result)


