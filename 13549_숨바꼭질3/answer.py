N = 2
K = 7

def solution(start):
    if N < K and N == 0:
        return K
    elif N > K and K == 0:
        return N
    global queue
    while queue:
        start = queue.pop(0)
        if start[0] == K:
            return start[1]
        queue.append([2 * start[0], start[1]])
        queue.append([start[0]-1, start[1]+1])
        queue.append([start[0]+1, start[1]+1])



queue = [[N, 0]]
print(solution([N, 0]))