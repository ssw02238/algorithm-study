import sys
sys.stdin = open('input.txt')

N = int(input())
timeline = [list(map(int, input().split())) for _ in range(N)]

timeline.sort(key=lambda x:(x[1], x[0]))
print(timeline)
# timeline
# [[0, 6], [1, 4], [2, 13], [3, 5], [3, 8], [5, 7], [5, 9], [6, 10], [8, 11], [8, 12], [12, 14]]
# [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

answer = 0
end_time = 0
for time in timeline:
    if end_time <= time[0]:
        end_time = time[1]
        answer += 1
print(answer)



