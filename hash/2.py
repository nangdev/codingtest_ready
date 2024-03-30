def solution(participant, completion):
    dic = {}

    for i in participant:
        dic[i] = 1
    
    for i in participant:
        dic[i] += 1
    
    for j in completion:
        dic[j] -= 2
    
    for k,v in dic.items():
        if v >= 1:
            return k