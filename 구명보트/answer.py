def solution(people, limit):
    answer = 0

    people.sort()
    idx = -1
    while people:
        if len(people) == 1:
            answer += 1
            return answer
        if people[idx] + people[0] <= limit:
            answer += 1
            people.pop(0)
            people.pop(-1)
        else:
            answer += 1
            people.pop(-1)
    return answer



people = [40, 50, 60, 90]
limit = 100
print(solution(people, limit))