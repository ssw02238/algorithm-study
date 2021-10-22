def solution(numbers, target):
    answer = [0] # 처음엔 계산 가공할거가 0이어야 해서
    for number1 in numbers:
        lst = []
        for number2 in answer:
            lst.append(number2+number1)
            lst.append(number2-number1)
        answer = lst
    return answer.count(target)

print(solution([1,1,1,1,1], 3))