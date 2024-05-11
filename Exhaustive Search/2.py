def solution(answers):
    answer = []
    a = [1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] * 1300
    c = [3,3,1,1,2,2,4,4,5,5] * 1000

    acnt, bcnt, ccnt = 0,0,0

    for i in range(len(answers)):
        if answers[i] == a[i]:
            acnt += 1
        
        if answers[i] == b[i]:
            bcnt += 1
        
        if answers[i] == c[i]:
            ccnt += 1
    
    
    m = max(acnt,bcnt,ccnt)

    if acnt == m:
        answer.append(1)
    if bcnt == m:
        answer.append(2)
    if ccnt == m:
        answer.append(3)

    return answer
