a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]

# 최후에 남는 풍선 개수 구하기
# 거의 다 큰 숫자만 터트린다고 생각하기
def solution(a):
    check = [0] * len(a)
    print(check)

    min_right, min_left = 999999, 9999999
    for i in range(len(a)):
        # 두 방향에서 살펴보고 check = 1 로 한번에 표시
        if a[i] < min_right:
            min_right = a[i]
            check[i] = 1
        if a[-1-i] < min_left:
            min_left = a[-i-1]
            check[-1-i] = 1
    return sum(check)

print(solution(a))
######################## 20/100 점 맞은 코드 ###############33
