def solution(n, words):
    answer = []  # 몇 번째 사람이 몇 번째 순서에 탈락?
    word = []  # 말한 단어들

    turn = 0
    while words:
        tmp = words.pop(0)
        if not word:
            word.append(tmp)
            turn += 1
        else:
            if tmp in word:
                answer = [(turn) % n + 1, (turn // n) + 1]
                return answer
            else:
                if word[-1][-1] == tmp[0]:
                    word.append(tmp)
                    turn += 1
                else:
                    # 끝말잇기 불가능 시
                    # turn+1 번째에 종료
                    answer = [(turn) % n + 1, (turn // n) + 1]
                    return answer
    answer = [0, 0]
    return answer