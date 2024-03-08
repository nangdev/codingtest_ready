def solution(s):
    temp = []
    
    for i in s:
        if temp and i == temp[-1]:
            temp.pop()
            continue
        
        temp.append(i)
    
    if temp:
        return 0
    else:
        return 1