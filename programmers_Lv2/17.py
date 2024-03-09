def solution(k, t):
    t.sort()
    ans = 0

    set_t = set(t)

    dic = []

    for i in set_t:
        dic.append(t.count(i))
    
    dic.sort(reverse=True)

    summ = 0
    for j in dic:
        summ += j
        ans += 1
        if summ >= k:
            break

    return ans