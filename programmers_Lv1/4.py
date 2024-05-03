def solution(N, stages):
    num = len(stages)
    dic = {}
    answer = []

    for i in range(1, N+1):
        n = stages.count(i)
        dic[i] = n/num
        if num-n != 0:
            num -= n
        else:
            num = 1

    prac = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    for p in prac:
        answer.append(p[0])

    return answer


print(solution(4, [4, 4, 4, 4, 4]))
