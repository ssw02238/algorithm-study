relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

from itertools import combinations

def solution(relation):
    row = len(relation) # 6
    col = len(relation[0])  # 4

    # 전체 조합 찾기
    candidates = []
    for i in range(1, col + 1): # 1 2 3 4
        candidates.extend(combinations(range(col), i))
    #print('조합들',candidates)

    # 유일성 검사
    unique = []
    for candidate in candidates:
        # 조합으로 구한 배열 내용을 다 담고 중복 체크 ***
        tmp = [tuple([item[i] for i in candidate]) for item in relation]
        #print(candidate, tmp)
        if len(set(tmp)) == row:
            unique.append(candidate)

    # 최소성 검사
    answer = set(unique)
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            # 하나가 다른 하나에 포함 된다면
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                # discard는 remove와 다르게 지정된 요소가 없어도 오류 안남
                answer.discard(unique[i])
    return len(answer)
print(solution(relation))