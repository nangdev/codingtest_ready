from collections import deque
def solution(cacheSize, cities):
    answer = 0
    arr = deque()
    N = len(cities)

    if not cacheSize:
        return 5 * N
    
    i = 0
    
    while len(arr) != cacheSize:
        c = cities[i].lower()

        if c not in arr:
            arr.append(c)
            answer += 5
        else:
            arr.remove(c)
            arr.append(c)
            answer += 1
        
        i += 1
        
    for n in range(i, N):
        c = cities[n].lower()

        if c not in arr:
            arr.popleft()
            arr.append(c)
            answer += 5
        else:
            arr.remove(c)
            arr.append(c)
            answer += 1

    return answer