import sys
sys.stdin = open('input.txt')


original = input()
bomb = input()

# 한 바퀴 돌기
def erase(bomb):
    global original
    idx_lst = []
    idx = 0
    while idx + len(bomb) <= len(original) + 1:
        if original[idx:idx+len(bomb)] == bomb:
            idx_lst.append([idx, idx+len(bomb)])
            idx = idx + len(bomb)
            # print(idx_lst)
        else:
            idx += 1
    if not idx_lst:
        return 0
    else:
        for i in range(len(idx_lst)-1, -1, -1):
            idx_a, idx_b = idx_lst[i][0], idx_lst[i][1]
            original = original[:idx_a] + original[idx_b:]
        return 1


while True:
    if not original:
        print('FRULA')
        break
    elif erase(bomb) == 0:
        print(original)
        break
    else:
        erase(bomb)




