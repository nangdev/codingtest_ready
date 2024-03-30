def solution(arr,a,b):
    serv1 = []
    serv2 = []

    for s in arr:
        serv1.append(s[0])
        serv2.append(s[1])
    

    serv1.sort()
    serv2.sort()

    N = len(serv1)
    cnt1,cnt2 = 0,0


    for i in range(N):
        cnt = 0
        for j in range(i+1,N):
            if serv1[i]*a >= serv1[j] and serv1[j]-(1000*b) <= serv1[i]:
                cnt += 1
            else:
                break
        
        cnt1 = max(cnt1,cnt)
    
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if serv2[i]*a >= serv2[j] and serv2[j]-(1000*b) <= serv2[i]:
                cnt += 1
            else:
                break

        cnt2 = max(cnt2, cnt)
    

    if cnt1 > cnt2:
        return [cnt1,1]
    else:
        return [cnt2,2]


print(solution([[2423,10],[3423,30],[1,40],[450,50],[1200,60],[2781,100]],2,1))