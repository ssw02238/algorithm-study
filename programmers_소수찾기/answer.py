from itertools import permutations
def solution(numbers):

    numbers = list(numbers)
    total_list = []
    for i in range(1, len(numbers)+1):
        num_lst = list(map(''.join, permutations(numbers, i)))
        total_list.append(num_lst)
    results = []
    for i in range(len(total_list)):
        for j in range(len(total_list[i])):
            num = total_list[i][j]
            while num[0] == '0':
                num = num[1:]
            results.append(num)

    results = list(set(results))
    print(results)
    cnt = 0
    for i in range(len(results)):
        if results[i]:
            num = int(results[i])
            if num == 1:
                pass
            else:
                flag = True
                for q in range(2, num):
                    if num % q == 0:
                        flag = False
                        break
                if flag:
                    cnt += 1

    return cnt
print(solution('0031'))

