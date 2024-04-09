def solution(msg):
    ans = []
    dic = {}

    for i in range(1,27):
        dic[chr(64+i)] = i
    
    n = 27
    idx = 0
    chk = False
    while True:

        ms = msg[idx]

        while True:
            if idx+1 == len(msg):
                chk = True
                break
            if ms + msg[idx+1] not in dic:
                ans.append(dic[ms])
                dic[ms + msg[idx+1]] = n
                n += 1
                idx += 1
                break
            else:
                ms += msg[idx+1]
                idx += 1
        
        if chk:
            ans.append(dic[ms])
        
        if idx == len(msg)-1:
            break

    if not chk:
        ans.append(dic[msg[-1]])

    return ans


print(solution("ABABABABABABABAB"))
