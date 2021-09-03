n = 6
times = [7, 10]

def solution(n, times):
    length = len(times)
    desk = [[] for _ in range(length)]
    people = [i+1 for i in range(n)]

    while people:
        person = people.pop(0)
        


print(solution(n, times))