relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

# 처음에 조합으로 구하려고 함
from itertools import combinations

def solution(relation):
    answer = 0

    # 후보 키 여부 확인할 index -------> [0, 1, 2, 3]
    idx = [i for i in range(len(relation[0]))]

    # 열 별로 모아보기
    content = []

    for i in range(len(relation[0])):
        lst = []
        for j in range(len(relation)):
            lst.append(relation[j][i])
        content.append(lst)
# content = [['100', '200', '300', '400', '500', '600'], ['ryan', 'apeach', 'tube', 'con', 'muzi', 'apeach'], ['music', 'math', 'computer', 'computer', 'music', 'music'], ['2', '2', '3', '4', '3', '2']]

    #  혼자로도 무결한 column일 경우 answer에 더함 / 아닐 경우 no_openkey에 더해둠
    no_openkey = {}
    for i in range(len(content)):
        target = content[i]
        if len(target) == len(set(target)):
            answer += 1
        else:
            # index 나중에 같이 저장하려고 임시방편으로 dict 형태로 저장
            no_openkey[i] = [-i]
    # {1: -1, 2: -2, 3: -3}
    print(no_openkey)

    # 2개 열 이상 후보키 다루기
    # 중복된 열을 어떻게 처리할까?
    # 중복된 열 중 중복된 index를 따로 저장하고 그 저장한 애들끼리 안 겹치면 같이 후보키 등극 가능
    for i in no_openkey:
        target = content[no_openkey[i]]
        for j in range(len(relation)):
            if target.count(target[j]) > 1:
                no_openkey[i-1].append(j)
    print(no_openkey)

    return answer


print(solution(relation))
