
def solution(a):
    result = [0 for _ in a]
    min_right, min_left = 999999, 9999999
    for i in range(len(a)):
        if a[i] < min_right:
            min_right = a[i]
            result[i] = True
        if a[-1-i] < min_left:
            min_left = a[-1-i]
            result[-1-i] = True
    return sum(result)

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))