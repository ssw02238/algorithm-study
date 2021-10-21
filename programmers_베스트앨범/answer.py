genres = ["classic", "pop", "classic", "classic", "pop"]
genres_clean = list(set(genres))
print(genres_clean)
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []
    music_cnt = [[] for _ in range(len(genres_clean))]
    genre_dict = {}
    for i in range(len(genres)):
        if genres[i] in genre_dict:
            genre_dict[genres[i]] += plays[i]
        else:
            genre_dict[genres[i]] = plays[i]
        music_cnt[genres_clean.index(genres[i])].append([i, plays[i]])
    sort_dict = list(genre_dict.items())
    sort_dict.sort(key=lambda x:-x[1])
    # [[[0, 500], [2, 150], [3, 800]], [[1, 600], [4, 2500]]]

    for i in range(len(music_cnt)):
        music_cnt[i].sort(key=lambda x:-x[1])
    print(sort_dict, music_cnt)

    for i in range(len(sort_dict)):
        genre = sort_dict[i][0]
        idx = genres_clean.index(genre)
        if len(music_cnt[idx]) == 1:
            answer.append(music_cnt[idx][0][0])
        else:
            for j in range(2):
                answer.append(music_cnt[idx][j][0])
    return answer
print(solution(genres, plays))