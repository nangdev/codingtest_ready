from collections import deque
def solution(brown, yellow):
    arr = deque()
    summ = brown + yellow

    for i in range(1,summ+1):
        if summ % i == 0:
            arr.append(i)
    
    lenarr = len(arr)
    if lenarr % 2 != 0:
        lenarr += 1

    for j in range(lenarr//2):
        if len(arr) == 1:
            a, z = arr[0], arr[0]
        else:
            a, z = arr.popleft(), arr.pop()

        if (z-2)*2 + a*2 == brown:
            return [z, a]
