def solution(clothes):
    ans = 1
    dic = {}
    for i in clothes:
        dic[i[1]] = 0

    for k in clothes:
        dic[k[1]] += 1

    for h in dic.values():
        ans *= (h+1)

    return ans-1
