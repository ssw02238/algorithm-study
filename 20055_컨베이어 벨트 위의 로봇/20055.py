import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, input().split())

container = deque(list(map(int, input().split())))
robot = deque([0] * N)

stage = 0

while True:
    container.rotate(1)
    robot.rotate(1)
    # print(container, robot)

    # 맨 마지막에는 바로 로봇 내려가기
    robot[-1] = 0

    if sum(robot):
        for i in range(-2, -N-1, -1):
            if robot[i] == 1 and robot[i + 1] == 0 and container[i + 1 - N] > 0:
                robot[i] = 0
                robot[i + 1] = 1
                container[i + 1 - N] -= 1
            robot[-1] = 0
    ## 해설 참고 (올라가는 위치에 로봇이 없을 때)
    if robot[0] == 0 and container[0] > 0:
        robot[0] = 1
        container[0] -= 1
    stage += 1
    if container.count(0) >= K:
        break
print(stage)