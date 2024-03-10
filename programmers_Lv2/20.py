def solution(want, number, discount):
    dic = dict(zip(want,number))
    ans = 0
    
    N = len(discount)
    wan = len(want)
    offset = N - 10 + 1

    for i in range(offset):
        temp = discount[i:10+i]

        count = 0
        for name in want:
            if temp.count(name) == dic[name]:
                count += 1
        
        if count == wan:
            ans += 1
    
    return ans