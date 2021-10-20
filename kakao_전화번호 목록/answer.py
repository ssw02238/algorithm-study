def solution(phone_book):
    idx = []
    for i in range(len(phone_book)):
        idx.append([phone_book[i], len(phone_book[i])])

    idx.sort(key=lambda x:x[1])
    for i in range(len(idx)):
        tmp = idx[i][0]
        for j in range(i+1, len(idx)):
            if tmp == idx[j][0][:len(tmp)]:
                print(tmp, idx[j][0])
                return False
    return True




print(solution(["12","123","1235","567","88"]))