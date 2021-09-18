def solution(w, h):
    # 원래 가능했던 사각형 갯수
    answer = w * h
    if w > h:
        x, y = w, h
    else:
        x, y = h, w

    # 더 긴게 x
    tmp = x // 3
    answer -= tmp * 4

    tmp = x % 3
    if tmp == 2:
        answer -= 3
    return answer


print(solution(5, 3))