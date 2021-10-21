array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer= []
for i in range(len(commands)):
    i, j, k = commands[i][0], commands[i][1], commands[i][2]
    tmp = array[i-1: j]
    tmp.sort()
    answer.append(tmp[k-1])
print(answer)