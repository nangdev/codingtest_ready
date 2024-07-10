from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()
    lis = deque(truck_weights)

    while lis:
        bridge.append(lis.popleft())

        if sum(bridge) > weight:
            lis.appendleft(bridge.pop())
        
        else:
            continue

    return answer
