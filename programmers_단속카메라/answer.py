def solution(routes):
    routes.sort(key=lambda x:x[0])
    answer = 0
    # [[-20, -15], [-18, -13], [-14, -5], [-5, -3]]
    while routes:
        tmp = routes.pop(0)
        while routes:
            if routes[0][0] <= tmp[1]:
                routes.pop(0)
            else:
                break
        answer += 1
    return answer

print(solution([[0,12],[1,12],[2,12],[3,12],[5,6],[6,12],[10,12]]))