citations = [0, 0, 0, 1]

def solution(citations):
    citations.sort()

    for i in range(citations[-1], -1, -1):
        for j in range(len(citations)):
            if citations[j] >= i:
                if len(citations[j:]) >= i:
                    return i
    # return result


print(solution(citations))