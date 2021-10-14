def solution(gems):
    type_n = len(set(gems)) # 종류의 개수
    gems_n = len(gems) # 주어진 보석들 수
    answer = []
    start, end = 0, 0 # 2개 포인터 설정
    dist,index = 0, 1 # 구간, index


    # 초기값
    gems_dict = {gems[0] : 1}
    while start < gems_n and end < gems_n:
        if len(gems_dict) < type_n:
            end += 1
            # 만약 끝까지 도달했다면 그대로 종료
            if end == gems_n:
                break
            gems_dict[gems[end]] = gems_dict.get(gems[end], 0) + 1
        else:
            answer.append((end-start, [start+1, end+1]))
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
    answer = sorted(answer, key=lambda x:(x[dist], x[index]))
    return answer[0][index]