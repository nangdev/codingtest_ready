def solution(prices):
    answer = []
    
    N = len(prices)

    for i in range(N-1):
        chk = True
        for j in range(i+1,N):
            if prices[j] < prices[i]:
                answer.append(j-i)
                chk = False
                break
        if chk:
            answer.append(N-1-i)

    answer.append(0)

    return answer