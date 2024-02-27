def solution(n):
    ans = 0

    for i in range(1,n+1):
        temp = 0
        for j in range(i,n+1):
            temp += j
            
            if temp > n:
                break
            else:
                if temp == n:
                    ans += 1
                    break
    
    return ans