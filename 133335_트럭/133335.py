import sys
sys.stdin = open('input.txt')

n, w, L = map(int, input().split())
# n은 트럭 수 / w는 다리 길이 / L은 다리 최대 하중

trucks = list(map(int, input().split()))
bridge = []

# [7, 4, 5, 6] [0, 0]
time = 0
while trucks:
    if len(bridge) < w:
        pass
    else:
        bridge.pop(0)


    if sum(bridge) + trucks[0] <= L:
        truck = trucks.pop(0)
        bridge.append(truck)
        time += 1
    else:
        bridge.append(0)
        time += 1


print(time + w)