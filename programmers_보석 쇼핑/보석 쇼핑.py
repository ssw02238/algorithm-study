def solution(gems):
    cnt = 999

    for i in range(len(gems)):
        gems_1 = list(set(gems))
        gem_cnt = [0 for _ in range(len(gems_1))]

        for j in range(i, len(gems)):
            if gem_cnt[gems_1.index(gems[j])] == 0:
                gem_cnt[gems_1.index(gems[j])] += 1
            if sum(gem_cnt) == len(gems_1):
                if j - i < cnt:
                    result = [i+1, j+1]
                    cnt = j - i
                break
    return result

gems = ["A", "B", "C", "B", "F", "D", "A", "F", "B", "D", "B"]
print(solution(gems))