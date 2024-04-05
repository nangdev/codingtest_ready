def solution(n, k):
    ans = 0
    jin = ''

    while n>0:
        mod = n%k
        n = n//k
        jin += str(mod)
    
    jin = jin[::-1]

    arr = jin.split('0')

    for i in arr:
        if i.isdigit():
            i = int(i)
        else:
            continue

        if i == 1:
            continue

        cnt = 0
        for a in range(1,i+1):
            if cnt >= 3:
                break
            if i % a == 0:
                cnt += 1
        
        if cnt == 2:
            ans += 1
    
    return ans

print(solution(110011,10))