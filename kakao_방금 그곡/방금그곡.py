import sys
sys.stdin = open('input.txt')

# 음악 제목, 시작 및 종료 시간, 악보
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "12:00,14:00,WORLD,ABCDEF"]

def solution(m, musicinfos):
    # m 전처리
    m = list(m)
    for i in range(len(m)):
        if m[i] == '#':
            m[i - 1] += '#'
    for item in m:
        if item == '#':
            m.remove('#')
    for i in range(len(m)):
        if m[i] == 'C#':
            m[i] = 'c'
        elif m[i] == 'D#':
            m[i] = 'd'
        elif m[i] == 'F#':
            m[i] = 'f'
        elif m[i] == 'G#':
            m[i] = 'g'
        elif m[i] == 'A#':
            m[i] = 'a'

    m = ''.join(m)

    musics = []
    # music infos 전처리
    for i in range(len(musicinfos)):
        target = musicinfos[i]
        a, b, c, d = target.split(',')
        # d 악보 전처리

        d = list(d)
        for idx in range(len(d)):
            if d[idx] == '#':
                d[idx - 1] += '#'
        for item in d:
            if item == '#':
                d.remove('#')
        for idx in range(len(d)):
            if d[idx] == 'C#':
                d[idx] = 'c'
            elif d[idx] == 'D#':
                d[idx] = 'd'
            elif d[idx] == 'F#':
                d[idx] = 'f'
            elif d[idx] == 'G#':
                d[idx] = 'g'
            elif d[idx] == 'A#':
                d[idx] = 'a'
        d = ''.join(d)

        time_gap = 0
        if a[:2] == b[:2]:
            time = int(b[3:]) - int(a[3:])
        elif a[3:] < b[3:]:
            time = (int(b[:2]) - int(a[:2])) * 60 + int(b[3:]) - int(a[3:])
        else:   # 1시 50분 ~ 2시 20분
            time = ((int(b[:2]) - 1) - int(a[:2])) * 60 + int(b[3:]) + 60 - int(a[3:])
        d = d*100
        d = d[: time]
        print('악보찡', d, len(d))
        musics.append([a, b, c, d, i])

    # [['12:00', '12:14', 'HELLO', 'CDEFGAB'], ['13:00', '13:05', 'WORLD', 'ABCDEF']]
    candidate = []
    for music in musics:
        time = 0
        if music[0][:2] == music[1][:2]:
            time = int(music[1][3:]) - int(music[0][3:])
        elif music[0][3:] < music[1][3:]:
            time = (int(music[1][:2]) - int(music[0][:2])) * 60 + int(music[1][3:]) - int(music[0][3:])
        else:   # 1시 50분 ~ 2시 20분
            time = ((int(music[1][:2]) - 1) - int(music[0][:2])) * 60 + int(music[1][3:]) + 60 - int(music[0][3:])
        music.append(time)
        if m in music[3]:
            candidate.append(music)
    # print(candidate)
    if len(candidate) == 1:
        return candidate[0][2]
    elif len(candidate) > 1:
        candidate.sort(key=lambda x:(-x[5], x[4]))
        return candidate[0][2]
    a = "(None)"
    return a

print(solution(m, musicinfos))

