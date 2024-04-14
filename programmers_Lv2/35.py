import heapq
from collections import deque
def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0

    while len(scoville) != 1:
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            return ans
        s2 = heapq.heappop(scoville)

        heapq.heappush(scoville, s1+s2*2)
        ans += 1
    
    if scoville[0] >= K:
        return ans
    else:
        return -1



def solution2(scoville, K):
    s = deque(sorted(scoville))
    ans = 0

    while True:
        s1 = s.popleft()
        if s1 >= K:
            return ans
        if not s:
            return -1
        
        s2 = s.popleft()

        s.appendleft(s1+s2*2)
        ans += 1




print(solution2([1, 2, 3, 9, 10, 12],7))
