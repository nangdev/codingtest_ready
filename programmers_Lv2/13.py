from collections import deque

def solution(people, limit):
    arr = deque(sorted(people))
    ans = 0

    while arr:
        if len(arr) == 1:
            ans += 1
            break

        if arr[0] + arr[-1] <= limit:
            arr.pop()
            arr.popleft()
            ans += 1
        else:
            arr.pop()
            ans += 1
    
    return ans


print(solution([50,70,80,50], 100))