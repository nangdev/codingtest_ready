def solution(participant, completion):
    dic = {}

    for i in participant:
        dic[i] = 0
    
    for i in participant:
        dic[i] += 1
    
    for j in completion:
        dic[j] -= 1
    
    for k,v in dic.items():
        if v == 1:
            return k