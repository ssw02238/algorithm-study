land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    n = len(land)
    idx = [[0,-1]]
    result = 0
    for i in range(n):
        tmp = land[i]
        find_maxi = []
        for j in range(4):
            find_maxi.append([tmp[j], j])
        find_maxi.sort()

        if find_maxi[-1][1] != idx[-1][1]:
            result += find_maxi[-1][0]
            idx.append(find_maxi[-1])
        else:
            result += find_maxi[-2][0]
            idx.append(find_maxi[-2])
        # print(result)
    return result

print(solution(land))