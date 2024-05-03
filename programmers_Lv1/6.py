def solution(lottos, win_nums):
    ans = [6,6,5,4,3,2,1]
    answer = []

    num = 0

    for i in lottos:
        if i in win_nums:
            num += 1
    
    answer.append(ans[num+lottos.count(0)])
    answer.append(ans[num])
    
    return answer