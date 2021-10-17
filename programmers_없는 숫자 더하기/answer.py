def solution(numbers):
    idx = 0
    result = 0
    numbers.sort()
    for num in range(10):
        if idx < len(numbers):
            if num == numbers[idx]:
                idx += 1
            else:
                result += num
        else:
            result += num
    return result