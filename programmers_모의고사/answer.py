answers = [1,3,2,4,2]

def solution(answers):
    cnt = len(answers) // 5 + 1
    first = [1, 2, 3, 4, 5] * cnt
    second = [2, 1, 2, 3, 2, 4, 2, 5] * cnt
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * cnt
    fi,se,th = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == first[i]:
            fi += 1
        if answers[i] == second[i]:
            se += 1
        if answers[i] == third[i]:
            th += 1
    result = []
    idx = max(fi, se, th)
    if fi == idx:
        result.append(1)
    if se == idx:
        result.append(2)
    if th == idx:
        result.append(3)
    return result
print(solution(answers))