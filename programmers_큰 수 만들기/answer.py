from itertools import combinations
def solution(number, k):
    number = list(map(int, number))
    n = len(number)
    n_lst = [_ for _ in range(n)]
    lst = list(combinations(n_lst, k))

    max_num = 0
    for num_set in lst:
        result = ''
        for i in range(n):
            if i in num_set:
                pass
            else:
                result += str(number[i])
        result = int(result)
        if result > max_num:
            max_num = result
    return int(max_num)

print(solution("4177252841", 4))