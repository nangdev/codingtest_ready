from collections import deque


def solution(priorities, location):
    p = deque(priorities)
    arr = deque()
    for i in range(len(p)):
        arr.append(i)

    cnt = 0
    while p:
        if p[0] != max(p):
            a = p.popleft()
            p.append(a)

            a = arr.popleft()
            arr.append(a)

        else:
            p.popleft()
            print(arr)
            b = arr.popleft()
            if b == location:
                cnt += 1
                break
            cnt += 1
        
    return cnt


print(solution([1, 1, 9, 1, 1, 1], 0))