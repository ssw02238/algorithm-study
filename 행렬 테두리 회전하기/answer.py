rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

def solution(rows, columns, queries):
    # 행렬 채우기
    matrix = [[] for _ in range(rows)]
    multip = 1
    while multip != rows+1:
        for i in range(1, 7):
            matrix[multip-1].append(6*(multip-1)+i)
        multip += 1
    result = []
    
    while queries:
        candidate = []
        x1, y1, x2, y2 = queries.pop(0)
        change_num = [matrix[x1][y1-1]]
        # 가로 1번
        for i in range(x1-1, x2-1):
            change_num.append(matrix[x1-1][i])
            candidate.append(change_num[0])
            matrix[x1-1][i] = change_num.pop(0)
        # 세로 1번
        for i in range(x1, x2):
            change_num.append(matrix[i][y2-1])
            matrix[i][y2-1] = change_num.pop(0)
            candidate.append(change_num[0])
        # 가로 2번
        for i in range(y2-2, y1-2, -1):
            change_num.append(matrix[x2-1][i])
            matrix[x2-1][i] = change_num.pop(0)
            candidate.append(change_num[0])
        # 세로 2번
        for i in range(x2-2, x1-2, -1):
            change_num.append(matrix[i][y1-1])
            matrix[i][y1-1] = change_num.pop(0)
            candidate.append(change_num[0])
        result.append(min(candidate))
    return result


print(solution(rows, columns, queries))