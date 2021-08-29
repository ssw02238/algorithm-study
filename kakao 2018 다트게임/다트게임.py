# 0~10점 얻기 가능 // 총 3번의 기회

# 1단계) 점수 3세트로 분류하기
dartResult = '1D2S3T*'

# 1-1 점수 위치만 알아내기
position = []
for i in range(len(dartResult)):
    # 근데 점수가 두자리수인 경우도 존재함..... (10점!!)
    if dartResult[i].isdigit() and not dartResult[i-1].isdigit():
        position.append(i)

# 1-2 점수 위치를 기준으로 SDT + 옵션까지 저장
score = []
for i in range(1, len(position)):
    score.append(dartResult[position[i-1]:position[i]])
score.append(dartResult[position[-1]:])
# print(score) #['1D', '2S', '3T*']

# 2단계) 점수 계산
result = []
for i in range(len(score)):
    # if len(score[i]) == 2:
    # option이 없을 경우로 조건 변경
    if '#' not in score[i] and '*' not in score[i]:
        point, q = int(score[i][:-1]), score[i][-1]
        if q == 'S':
            result.append(point)
        elif q =='D':
            result.append(point **2)
        else:
            result.append(point ** 3)
    else:
        point, q, option = int(score[i][0]), score[i][1], score[i][2]
        if q == 'S':
            result.append(point)
        elif q =='D':
            result.append(point **2)
        else:
            result.append(point ** 3)

        if option == '*':
            # 처음으로 스타상 딸때 아닐때 구분
            if len(result) >= 2:
                result[-1] = result[-1] * 2
                result[-2] = result[-2] * 2
            else:
                result[-1] = result[-1]*2
        elif option == '#':
            result[-1] = result[-1] * -1
print(result)
print(sum(result))

