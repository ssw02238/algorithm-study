sizes = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]

def solution(sizes):
    a, b = 0, 0
    width = []
    height = []
    for i in range(len(sizes)):
        width.append(sizes[i][0])
        height.append(sizes[i][1])
    a = max(max(width), max(height))

    for i in range(len(sizes)):
        tmp = sizes[i]
        if min(tmp[0], tmp[1]) > b:
            b = min(tmp[0], tmp[1])
    return a * b

print(solution(sizes))