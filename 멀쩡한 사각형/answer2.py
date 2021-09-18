def solution(w, h):
    # 원래 가능했던 사각형 갯수
    answer = w * h
    if w > h:
        x, y = w, h
    else:
        x, y = h, w

    # 더 긴게 x , 작은게 y
    if x % y == 0:
        answer -= x
    elif y == 1:
        answer = 0
    else:
        if x % 2 == 0:
            answer -= y * (x // 2)
        else:
            answer -= y * ((x+1) // 2)
    return answer


print(solution(2, 7))