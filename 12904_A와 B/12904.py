import sys
sys.stdin = open('input.txt')

S = input()
T = input()

result = 0
queue = [S]
tmp = S
while len(tmp) <= len(T):
    tmp = queue.pop(0)
    # 규칙 1
    a = tmp + 'A'
    # 규칙 2
    b = list(reversed(list(tmp)))
    b.append('B')
    b1 = ''
    for i in range(len(b)):
        b1 += b[i]

    # 확인
    if a == T or b1 == T:
        result = 1
        break
    else:
        queue.append(a)
        queue.append(b1)
print(result)


