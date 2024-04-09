def solution(scoville, K):
    s = sorted(scoville,reverse=True)
    ans = 0

    while s[-1] < K:
        s1 = s.pop()
        s2 = s.pop()
        
        s.append(s1 + s2*2)
        ans += 1
    
    return ans


print(solution([1, 2, 3, 9, 10, 12],7))
