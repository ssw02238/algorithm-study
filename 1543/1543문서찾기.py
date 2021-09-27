import sys
sys.stdin = open('input.txt')

word = input()
tmp = input()


answer = 0
idx = []
queue = []
# [[0, 2], [2, 4], [4, 6], [6, 8]]

for i in range(len(word)-len(tmp)+1):
    if word[i:i+len(tmp)] == tmp:
        # 시작과 끝 지점 저장
        idx.append([i, i+len(tmp)-1])


if len(idx) >= 2:
    queue = idx[0]
    for j in range(1, len(idx)):
        target = idx[j]
        if target[0] > queue[1]:
            answer += 1
            queue = target
    answer += 1
elif len(idx) == 1:
    answer += 1
else:
    pass

print(answer)
