orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
from itertools import combinations
#조건 - 최소 2개 이상 단품 메뉴 구성 + 2명 이상의 손님으로부터 주문되어야 함

def solution(orders, course):
    result = [] # 코스 요리로 만들 음식 리스트들을 오름 차순 정렬

    for i in range(len(orders)):
        order = orders.pop(0)
        orders.append(list(order))

    for cnt in course:
        combination = {}
        for i in range(len(orders)):
            combis = list(combinations(orders[i], cnt))
            for j in range(len(combis)):
                combis[j] = list(combis[j])
                combis[j].sort()
                combis[j] = tuple(combis[j])
                if combis[j] not in combination:
                    combination[combis[j]] = 1
                else:
                    combination[combis[j]] += 1
        print(cnt, '개 뽑기', combination)
        sc = sorted(combination.items(), key=lambda x:x[1], reverse=True)
        for i in range(len(sc)):
            if sc[0][1] >= 2:
                if sc[i][1] == sc[0][1]:
                    pick = ''
                    for word in sc[i][0]:
                        pick += word
                    result.append(pick)
                else:
                    break

    result.sort()
    return result


print(solution(orders, course))