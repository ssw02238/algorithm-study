s = "abcabcdede"

# 약수 구하기
multiple = []
for i in range(1, len(s)):
    if len(s) % i == 0:
        multiple.append(i)
multiple.reverse()
print(multiple)
# multiple = [4, 2, 1]
min = 999999
for number in multiple:
    slice = []
    result = 0 # 축약된 길이
    for i in range(len(s)//number):
        slice.append(s[number*i:number*i+number])
    print(slice)
    start = 0 # 기준 idx
    group = 0 # 중복되는 거 개수
    group_cnt = 0
    for i in range(1, len(slice)):
        if slice[i] == slice[start]:
            group += 1
            group_cnt += 1
        else:
            start = i
    print(group_cnt)
    GB = group - len(set(slice))
    result = len(s) - GB
    if result < min:
        min = result

print(min)