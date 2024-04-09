def solution(n, t, m, p):
    ans = ''
    num = 0
    idx = 0
    D = ""

    while len(ans) != t:

        while num != 0:
            D += str(num % n)
            num //= n
        
        D = D[::-1]

        for i in D:
            if (idx % m) + 1 == p:
                ans += i
            idx += 1
            
        num += 1

    return ans

print(solution(2,4,2,1))
