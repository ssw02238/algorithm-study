table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

def solution(table, languages, preference):
    # score_table > 점수 테이블
    score_table = []
    for i in range(len(table)):
        row = table[i]
        score_table.append(list(row.split()))

    # 5개 테이블을 모두 돌면서 점수 체크
    max_score = 0
    for i in range(5):
        target = score_table[i]
        score = 0
        for j in range(len(languages)):
            language = languages[j]
            if language in target:
                score += (6 - target.index(language)) * preference[j]
        if score > max_score:
            max_score = score
            result = score_table[i][0]
        elif score == max_score:
            if target[0] <= result:
                result = target[0]
        else:
            pass
    return result


print(solution(table, languages, preference))