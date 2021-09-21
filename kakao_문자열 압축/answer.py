s = "xababcdcdababcdcd"
min = 999999
for number in range(len(s)//2, 0, -1):
    slice = []
    result = 0 # 축약된 길이
    for i in range(len(s)//number):
        slice.append(s[number*i:number*i+number])
    if len(s) % number != 0:
        slice.append(s[number*i+number:])
    # print(slice)

    start = 0 # 기준 idx
    remove = 0 # 중복되는 거 개수
    group_cnt = 0
    if slice[0] == slice[1]:
        group_cnt += 1
    for i in range(1, len(slice)):
        if slice[i] == slice[start]:
            remove += 1
        elif slice[i] != slice[start] and i != (len(slice)-1):
            if slice[i] == slice[i+1]:
                start = i
                group_cnt += 1
            else:
                start = i
        else:
            start = i

    # print(number, remove, group_cnt)
    result = len(s) - (number * remove) + group_cnt
    # print(result)
    if result < min:
        min = result

print(min)