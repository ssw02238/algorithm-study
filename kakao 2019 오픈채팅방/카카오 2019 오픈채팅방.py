record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

def solution(record):
    result = []
    dict = {}
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

    answer = []
    for i in range(len(result)):
        id = result[i][0]
        answer.append(dict[id]+result[i][1])
    return answer

print(solution(record))