import sys
sys.stdin = open('input.txt')

H, W = map(int, input().split())
blocks = list(map(int, input().split()))
# [3, 0, 1, 4]
left = 0
right = W - 1

max_left = blocks[left]
max_right = blocks[right]

answer = 0

while left < right:
    max_left = max(max_left, blocks[left])
    max_right = max(max_right, blocks[right])

    if max_right >= max_left:
        answer += max_left - blocks[left]
        left += 1
    else:
        answer += max_right - blocks[right]
        right -= 1
print(answer)
