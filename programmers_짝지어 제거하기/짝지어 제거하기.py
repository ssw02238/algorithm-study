s = 'a'

def solution(s):
    s = list(s)
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            i = 0
        else:
            i += 1
        if not s:
            return 1
    return 0

print(solution(s))