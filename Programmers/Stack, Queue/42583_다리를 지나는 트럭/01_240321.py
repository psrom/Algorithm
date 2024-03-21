# https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque


def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    current = 0
    while truck_weights:
        time += 1

        current -= bridge.popleft()
        p = truck_weights.popleft()

        if current + p <= weight:
            current += p
            bridge.append(p)

        else:
            truck_weights.appendleft(p)
            bridge.append(0)
    time += bridge_length

    return time
