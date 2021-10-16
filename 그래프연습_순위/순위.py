def solution(n, results):
    fix = 0
    win, lose = [[] for _ in range(n)], [[] for _ in range(n)]
    for i in range(len(results)):
        winner, loser = results[i][0], results[i][1]
        # 내가 이긴 애들 (내가 얘네들 이김)
        win[winner-1].append(loser)
        # 내가 진  애들 ( 내가 얘네들 한테 짐)
        lose[loser-1].append(winner)
    print(win, lose) # [[2], [5], [2], [3, 2], []] [[], [4, 3, 1], [4], [], [2]]
    for i in range(n):
        for winning in win[i]:
            # 내가 이긴 애들한테 진 애들도 내가 이긴거야
            for tmp in lose[i]:
                if tmp not in lose[winning-1]:
                    lose[winning-1].append(tmp)
        for losing in lose[i]:
            for tmp in win[i]:
                if tmp not in win[losing-1]:
                    win[losing-1].append(tmp)
    print(win, lose)
    for i in range(n):
        if len(win[i]) + len(lose[i]) == n-1:
            fix += 1
    return fix
