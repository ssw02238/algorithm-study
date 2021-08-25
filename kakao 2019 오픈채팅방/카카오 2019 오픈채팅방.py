record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    # result > id와 문구를 같이 저장
    result = []
    ['userid', 님이 들어왔습니다]
    # dict > id 별로 닉네임을 같이 저장
    dict = {}

    # 아이디 별로 문구랑 닉네임을 저장만 시켜둠
    for i in range(len(record)):
        a = record[i].split()
        if a[0] == 'Enter':
            command, id, nickname = a[0], a[1], a[2]
            dict[id] = nickname
            result.append([id, "님이 들어왔습니다."])
        elif a[0] == "Leave":
            command, id = a[0], a[1]
            result.append([id, "님이 나갔습니다."])
        else:
            command, id, nickname = a[0], a[1], a[2]
            dict[id] = nickname

    # answer > 답으로 나올 변수
    answer = []
    # result를 다시 돌면서 닉네임 일괄 수정
    for i in range(len(result)):
        id = result[i][0]
        answer.append(dict[id]+result[i][1])
    return answer

print(solution(record))

# 소요시간 14분
#### 마음 급해서 정말 비효율적으로 풀었다고 생각했는데 일단 정확성만 채점 기준이라 다 맞은걸로 돌아가긴 했습니다.....